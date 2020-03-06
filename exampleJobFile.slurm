#!/bin/bash
##ENVIRONMENT SETTINGS; CHANGE WITH CAUTION
#SBATCH --export=NONE                #Do not propagate environment
#SBATCH --get-user-env=L             #Replicate login environment

##NECESSARY JOB SPECIFICATIONS
#SBATCH --job-name=Example_1       #Set the job name to "JobExample1"
#SBATCH --time=1-1:30:00              #Set the wall clock limit to 1 day 1hr and 30min
#SBATCH --ntasks=1                   #Request 1 task
#SBATCH --mem=2560M                  #Request 2560MB (2.5GB) per node
#SBATCH --output=output/Example_1Out.%j      #Send stdout/err to "Example1Out.[jobID]"

##OPTIONAL JOB SPECIFICATIONS
#SBATCH --account=122749065275             #Set billing account to 123456
#SBATCH --mail-type=ALL              #Send email on all job events
#SBATCH --mail-user=test@email.com    #Send all emails to email_address

#First Executable Line
echo "starting at `date` on `hostname`"
echo "SLURM_JOBID=$SLURM_JOBID"

# main job
env | grep SLURM
WORKDIR=$SCRATCH/HPRC-Python3.7-Example

######## Set up
# load Python
# module load Python/3.7.0-intel-2018b
# create Virtual Env
# cd $WORKDIR
# create virtual environment to install your own package
# virtualenv venv


######### Activate
# go to project foler
cd $WORKDIR
# activate environment
source venv/bin/activate
python test.py
echo "ended at `date` on `hostname`"
exit 0