#!/bin/bash

lxc launch base server
lxc launch base client0
lxc launch base client1

lxc file push server.conf  server/etc/wireguard/
lxc file push client0.conf client0/etc/wireguard/
lxc file push client1.conf client1/etc/wireguard/
