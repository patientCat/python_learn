# Anaconda

https://conda.io/projects/conda/en/latest/user-guide/getting-started.html

## miniconda
使用miniconda 精简版

conda create -n demo python=3.8.5

conda init 激活conda

conda activate demo

conda install package
conda uninstall package

## 如何将conda环境和jupyter环境关联
demo 代表环境名称
python -m ipykernel install --user --name demo --display-name "demo"