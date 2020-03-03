#!/bin/bash
##ENVIRONMENT SETTINGS; CHANGE WITH CAUTION
SBATCH --export=NONE                #Do not propagate environment
SBATCH --get-user-env=L             #Replicate login environment

##NECESSARY JOB SPECIFICATIONS
SBATCH --job-name=pyExample_1       #Set the job name to "JobExample1"
SBATCH --time=01:30:00              #Set the wall clock limit to 1hr and 30min
SBATCH --ntasks=1                   #Request 1 task
SBATCH --mem=2560M                  #Request 2560MB (2.5GB) per node
SBATCH --output=pyExample_1Out.%j      #Send stdout/err to "Example1Out.[jobID]"

##OPTIONAL JOB SPECIFICATIONS
SBATCH --account=122749065275             #Set billing account to 123456
SBATCH --mail-type=ALL              #Send email on all job events
SBATCH --mail-user=diya.li@tamu.edu    #Send all emails to email_address

#First Executable Line
env | grep SLURM
./init.sh