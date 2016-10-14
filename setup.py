#!/usr/bin/env python
#Hardcoded dependancy installer

import os 


libpq = "apt-get install libpq-dev"
python3 = "apt-get install python3"
python3dev = "apt-get install python3-dev"
psycopg2 = "apt-get install python-psycopg2"

os.system(libpq)
os.system(python3)
os.system(python3dev)
os.system(psycopg2)
