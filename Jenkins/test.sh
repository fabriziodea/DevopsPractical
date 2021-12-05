#!/bin/bash

sudo apt update
sudo apt-get install -y python3-pip python3-venv
python3 -m venv venv
source venv/bin/activate
pip3 install -r test-requirements.txt

# Test Service1
cd service1
python3 -m pytest --cov=application
cd ..

# Test Service2
cd service2
python3 -m pytest --cov=application
cd ..

# Test Service3
cd service3
python3 -m pytest --cov=application
cd ..

# Test Service4
cd service4
python3 -m pytest --cov=application
cd ..

deactivate