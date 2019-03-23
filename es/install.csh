#!/bin/bash
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.6.1.deb
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.6.1.deb.sha512
shasum -a 512 -c elasticsearch-6.6.1.deb.sha512 
sudo dpkg -i elasticsearch-6.6.1.deb
