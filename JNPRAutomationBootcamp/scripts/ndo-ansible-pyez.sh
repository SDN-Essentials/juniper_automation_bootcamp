#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install -y python-dev libxml2-dev python-pip libxslt-dev build-essential libssl-dev libffi-dev libffi-dev
sudo pip install --upgrade setuptools
sudo pip install cryptography==1.2.1 junos-eznc ansible==2.3.2.0 jxmlease
sudo ansible-galaxy --force install Juniper.junos,1.4.3
