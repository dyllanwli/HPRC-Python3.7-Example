#!/bin/bash

# This scripts is a happy path for running python program on HPRC

# loging to your machine with you netid and pass first.


######## Set up
# load Python
module load Python/3.7.0-intel-2018b
# create Virtual Env
cd $SCRATCH
# create new directory
mkdir python_project
cd python_project
# create virtual environment to install your own package
virtualenv venv


######### Activate
# go to project foler
cd $SCRATCH/python_project
# activate environment
source venv/bin/activate
# check the pip list
# pip list

######### Install package
pip install numpy
pip install pymongo
# check pip list
# pip list

######### Deactivate
deactivate 
