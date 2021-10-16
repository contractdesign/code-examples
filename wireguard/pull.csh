#!/bin/bash


lxc file pull server/etc/wireguard/server.conf server.conf
lxc file pull client0/etc/wireguard/client0.conf client0.conf
lxc file pull client1/etc/wireguard/client1.conf client1.conf
