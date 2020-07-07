# Proxying SSH with nginx

This compose file exercises proxying of SSH through an nginx reverse proxy.  It brings up a container running Ubuntu 16.04 running sshd and
a second container with nginx.

# Running

To bring up the containers,
```
$ docker-compose up
```

Then, you can ssh to the nginx host

```
$ ssh root@172.28.1.2
```

nginx proxies to the connection to the Ubuntu host at address 172.28.1.3.
