
#
# based on
# https://github.com/dockerfile/ubuntu/blob/master/Dockerfile
#
FROM ubuntu:14.04

RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y openssh-server && \
  rm -rf /var/lib/apt/lists/* && \
  adduser --disabled-password --gecos "" ubuntu


COPY ./id_rsa.pub /home/ubuntu/.ssh/authorized_keys
RUN chown ubuntu /home/ubuntu/.ssh/authorized_keys

ENV HOME /home/ubuntu
WORKDIR /home/ubuntu



# bash is invoked to keep the container from exiting
USER root
CMD /etc/init.d/ssh start && bash

