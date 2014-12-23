#!/bin/bash
vagrant init puphpet/debian75-x64
vagrant up
vagrant ssh
wget https://www.python.org/ftp/python/3.4.2/Python-3.4.2.tar.xz
tar xf Python-3.4.2.tar.xz
cd Python-3.4.2
sudo aptitude install gcc
./configure --prefix /opt/python/3.4.2
sudo make
sudo make install
export PATH=/opt/python/3.4.2/bin:$PATH
cd ..
pyvenv fb1
source fb1/bin/activate
