# Firefox over VNC
#
# VERSION               0.1
# DOCKER-VERSION        0.2

# $ docker build -t firefox-vnc .
# $ docker run -p 5900 firefox-vnc x11vnc -forever -usepw -create

# TODO how to tell which versions of ubuntu are available?
#FROM    ubuntu:12.04
FROM    ubuntu:14.04
# Make sure the package repository is up to date
RUN     echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN     apt-get update

# Install vnc, xvfb in order to create a 'fake' display and firefox
RUN     apt-get install -y x11vnc xvfb firefox

RUN     mkdir ~/.vnc
# Setup a password
RUN     x11vnc -storepasswd 1234 ~/.vnc/passwd
# Autostart firefox (might not be the best way to do it, but it does the trick)
RUN     bash -c 'echo "firefox" >> /.bashrc'
