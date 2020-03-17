#!/bin/bash

# This scripts is a happy path for running python program on HPRC using nohup

module load Python/3.7.0-intel-2018b

virtualenv venv

source venv/bin/activate

nohup python test.py & >> nohup.out

######### Deactivate
# deactivate 
