#!/bin/bash

# conda create env -f environment fail
# 手动执行

conda create -n demo python=3.8.5
conda activate demo

conda install jupyterlab
conda install numpy
conda install matplotlib
conda install pytorch::pytorch torchvision torchaudio -c pytorch