# Jupyter

## 处理Jupyter Kernel died
一般是因为import 包的问题。
uninstall, 然后install解决。

如果不行。 就换个方式安装。比如pytorch

conda install pytorch 不行，会导致kernel died
去conda官网，其有推荐，重新安装即可。大概率是因为之前版本太低
https://pytorch.org/get-started/locally/