# Running OpenVPN on an AWS EC2 instance

This file sets up an Amazon Web Services (AWS) EC2 instance with an
OpenVPN is static key mode.  It is based on this
[post](https://openvpn.net/index.php/open-source/documentation/miscellaneous/78-static-key-mini-howto.html)
from the OpenVPN website.  In this situation, the AWS EC2 instances is the
**server** and the machine which is tunneling to it is the **client**.

# To Configure the Client and Server

1. **client**: Modify `client.conf` to reference the IP address of the EC2 instance

2. **client**: Generate the secret key
```
    $ openvpn --genkey --secret static.key
```
3. **server**: Create an EC2 instance and note its IP address
(`${AWS_IP}` below).  When creating the EC2 instance, make sure to add
a security group rule to allow UDP traffic from port 1194 in addition
to the default SSH port 22 rule.  Adding this rule allows OpenVPN
traffic to pass to the instance.

4. **server**: Copy `server.conf` and the secret key file, `static.key`, created in step 2.
```
    $ scp server.conf ubuntu@${AWS_IP}:/home/ubuntu
    $ scp static.key  ubuntu@${AWS_IP}:/home/ubuntu
```



5. **server**: Configure server to route incoming packets
```
    $ sysctl -w net.ipv4.ip_forward=1
```

6. **server**: Configure server to NAT packets
```
    $ iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE 
```

7. **server**: Start openvpn on the server.  The server has to be ready so that it can accept an incoming connection from the client.
```
    $ sudo openvpn --config server.conf
```

8. **server**: Start openvpn on the client.
```
    $ sudo openvpn --config client.conf
```

After a few seconds, the log files should indicate that the connection
has been initiated.


## To Verify Connection

To verify that traffic is being forwarded from the VPN tunnel, check
that the IP address on the **client** matches that of the server:
```
    $ curl ifconfig.co
```
