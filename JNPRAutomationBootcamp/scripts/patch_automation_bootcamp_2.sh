#!/usr/bin/env bash

sudo ip r a 10.11.12.1/32 via 172.16.0.1
sudo ip r a 10.11.12.2/32 via 172.16.0.2

sudo apt-get install libssl1.0.0/trusty libssl-dev/trusty openssl/trusty
sudo apt-get install -y python-dev libxml2-dev python-pip libxslt-dev build-essential libssl-dev libffi-dev libffi-dev
sudo apt-get install sqlite3 libsqlite3-dev


sudo apt-get install  libssl1.0.0/trusty libssl-dev/trusty openssl/trusty
sudo apt-get install -y python-dev libxml2-dev python-pip libxslt-dev build-essential libssl-dev libffi-dev libffi-dev
sudo apt-get install -y sqlite3 libsqlite3-dev
sudo pip install --upgrade setuptools
sudo pip install --upgrade setuptools pip
sudo pip install markupsafe
sudo pip install cryptography==1.2.1 junos-eznc ansible==2.3.2.0 jxmlease
sudo ansible-galaxy --force -c install Juniper.junos,1.4.3
sudo chown -R chuck:chuck ~/.ansible
