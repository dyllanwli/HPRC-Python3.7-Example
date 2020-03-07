#!/bin/bash

# This scripts is a happy path for running python program on HPRC

# loging to your machine with you netid and pass first.

WORKDIR=$SCRATCH/HPRC-Python3.7-Example

######## Set up
# load Python
module load Python/3.7.0-intel-2018b
# create Virtual Env
cd $WORKDIR
# create virtual environment to install your own package
virtualenv venv


######### Activate
# go to project foler
cd $WORKDIR
# activate environment
source venv/bin/activate

######### Install package
# pip install numpy
pip install tweepy
pip install python-daemon
pip list
python test.py

######### Deactivate
# deactivate 
