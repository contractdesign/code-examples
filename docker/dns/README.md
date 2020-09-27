
# Domain Name Resolution in Docker

To be useful, containers in Docker must have a way to find each other.  The containers's IP addresses could change from run to run, so a logical way of doing service discovery is for the containers to refer to each other by domain names.

The version of docker tested (19.03.12) uses DNS to resolve domain names.  Earlier docker versions modified each container's `/etc/hosts` file instead.

To create a DNS entry for your container, set your container label to its FQDN.  For example, to have your container accessed as either `test_1` or `test_1.com`, create an entry in the docker-compose file as follows,
```
services:
...
   www.test_1.com
      image: alpine
      ...
```

Domain names not defined in the compose file can be added explicitly ([ref](https://stackoverflow.com/questions/29076194/using-add-host-or-extra-hosts-with-docker-compose)).  These entries do not appear in `/etc/hosts` but are being resolved through DNS.

```
services:
...
   www.test_1.com
      image: alpine
      ...
      extra_hosts:
        - "testhost.com:8.8.8.8"

```

Curiously, no DNS queries appeared when I wireshark'd all interfaces.  Doing nslookup shows the DNS server as `127.0.0.11:53`.



The docker-compose directive `hostname` does not create a DNS entry.  It sets the hostname so that the `hostname` command works (see [docs](https://docs.docker.com/config/containers/container-networking/)).

The docker-compose directive `container_name` sets the name of the container for access by docker CLI commands, e.g.,
```
$ docker exec -it <name> /bin/ash
```


The docker-compose file assigns the first two containers names using `container_name`.  For example, to access `test_1`, do
```
$ docker exec -it test_1 /bin/ash
```

Container `test_3` can be accessed by its automatically assigned name `dns_test_3_X`, where X is an integer.


# Testing

This sections summarizes testing I did to confirm my understanding of the above.

## Container "test_1.com"

From this container (`docker exec -it <ID> /bin/ash`) pinging
- `test_1` and `test_1.com` both work
- `test_2` works, `test_2.com` does *not* work

- `hostname` run in the container returns 08f0ec809XXX

The contents of `/etc/hosts` is:
```
...
172.21.0.2      08f0ec809XXX
```

## Container "test_2"

From this container,
- `test_1` and `test_1.com` both work
- `test_2` works, `test_2.com` both work
-  `www.test_3.com` works, `test_3.com` does *not* work

hostname returns `test_2.com`


The contents of `/etc/hosts` is:
```
...
172.21.0.3      test_2.com test_2
```
