# LearnPytorch

## 矩阵本质
Pytorch的矩阵本质和numpy区别不大。

只要对numpy.array有理解，即可理解torch.tensor。差异不大。

## torch.autograd
如何理解自动求导?

训练神经网络本质分为2步：
1. forward propagation : 前向计算，猜测损失函数的值
2. backward propagation : 反向传播，求得损失函数对参数的导数

得到导数后，我们就可以利用SGD来进行参数优化了


## FAQ

### 1. mat1 and mat2 must have the same dtype, but got Double and Float
https://discuss.pytorch.org/t/runtimeerror-mat1-and-mat2-must-have-the-same-dtype/166759/5

default model.weight and bias are torch.float32

