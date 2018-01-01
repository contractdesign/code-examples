# SSH'ing into a container

This Dockerfile creates a container which you can access using SSH.  It
first requires that your public key (id_rsa.pub) is placed into this
directory.

To build and run the container do the following:

```
   $ make build
   $ make run
```

Once running, to ssh into the container, first identify the IP address
of the container.  To do this, find the container id
```
   $ docker ps  # returns all container ids.  find that of your container
   $ docker inspect <container id> | grep IPAddress
```

See [stackoverflow](https://stackoverflow.com/questions/17157721/how-to-get-a-docker-containers-ip-address-from-the-host) for more information.

Then, SSH into it:


```
   $ ssh ubuntu@172.17.0.2 # use address from preceeding step
```
