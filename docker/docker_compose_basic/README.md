
# Sample Docker Compose File

This directory contains a simple docker-compose.yml file that brings
up three hosts that can be SSH'd into.

To bring up the containers,

```
    $ docker-compose up
```

To terminate running containers and clean up after then
```
    $ docker-compose ps  # see what's running
    $ docker-compose kill
    $ docker-compose rm -f
```
