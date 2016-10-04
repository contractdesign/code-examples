#!/bin/bash

ansible-playbook ./setup.yml -v -vvvv -u ubuntu -i ./host.yml --private-key=~/keys/exp.pem
