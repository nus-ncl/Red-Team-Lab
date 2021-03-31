#! /usr/bin/bash

sudo apt-get update
sudo apt-get install python3-pip -y

cd /opt && git clone https://github.com/SecureAuthCorp/impacket.git
cd /opt/impacket && sudo pip install .
cd /opt/impacket && sudo python setup.py install && sudo python3 setup.py install