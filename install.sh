#!/bin/bash

# Install essential packages from Apt
apt-get update -y

# Python dev packages
apt-get install -y build-essential python python-dev python-setuptools python-pip

# Git
apt-get install -y git

pip install -r /vagrant/requirements.txt

# Cleanup
apt-get clean
