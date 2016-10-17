#!/bin/bash

ansible-playbook ./setup.yml -u ubuntu -i ./host.yml --private-key=~/keys/exp.pem
