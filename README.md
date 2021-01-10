# HPRC custom setup
custom setup

need to need to move your ~/.conda directory to $SCRATCH and make a symbolic link since Anaconda3 may fill up your $HOME disk quota:
```
cd ~
mv .conda $SCRATCH
ln -s $SCRATCH/.conda


mv .local $SCRATCH
ln -s $SCRATCH/.local
```

crete env
```
ml purge
module load Anaconda3/2020.11
conda create -n jupyterlab_2
```
