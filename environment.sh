#!/bin/bash
sudo apt-get install postgresql postgresql-contrib
psql facebook < facebook.sql
sudo apt-get install python3-pip
sudo apt-get install libpq-dev
sudo pip3 install psycopg2
sudo pip3 install -r requirements.txt