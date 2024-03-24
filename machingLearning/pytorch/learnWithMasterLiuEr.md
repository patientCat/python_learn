# pytorch

参考：刘二大人
https://www.bilibili.com/video/BV1Y7411d7Ys/?spm_id_from=333.337.search-card.all.click&vd_source=842b1225f5d953c8df3fd60918cd05ff

先实践，再学习
## 环境配置

python3 -m pip install -U pip
python3 -m pip install -U matplotlib
#### 对齐jupyter

https://stackoverflow.com/questions/75498337/adding-jupyter-nbextensions-configurator-to-jupyter-notebook
jupyter notebook --version 确认版本 
更新jupyter版本
python3 -m pip install -U notebook==6.4.12
安装插件
conda install -c conda-forge jupyter_nbextensions_configurator
conda install -c conda-forge jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
jupyter nbextensions_configurator enable --user


## 01线性模型

4大要素
1. 数据集
2. MODEL
3. 训练
4. 预测

### 数据集

训练数据
测试数据

如果拿不到测试数据的结果。一般选择将训练数据分为：训练数据 + 开发数据。
用子训练数据训练模型，拿开发数据进行验证。如果表现较好，再拿所有训练数据训练模型，去提交给测试数据验证（一般在比赛这么做）

### 训练问题
可视化问题
visdom

断点重试问题
即模型持久化

### 练习
通过使用穷举法，观察法，求得模型的最佳参数。并绘图。

## 02梯度下降法

> 梯度的方向：是函数值变化最快的方向。正方向找极大值，反方向找极小值
### 损失函数
损失函数只是用来训练模型，让模型有目标的函数。具体的值多少没有意义。保证恒大于等于0即可。

有时候，我们会拿(y_hat - y)^2作为损失函数。
有时候，我们会拿MSE作为损失函数。二者之间是线性关系。 
根据公式可知，影响的是对损失函数求偏导的常数项。一般以 (y_hat - y)^2 / 2M 作为损失函数。目的是让偏导后的结果和分母的2化解掉。


梯度下降算法只能找到局部最优。
如何解决鞍点问题。

训练损失有噪声，可以进行加权平滑
加权平滑？为什么要加权平滑。

### 优化
梯度下降算法，可以利用并行性能。时间复杂度好。但容易陷入鞍点。
随机梯度下降算法，不容易陷入鞍点，但是时间复杂度差，因为w_i+1 依赖 w_x，不能并行。
所以使用mini-batch，结合二者。


## 03反向传播
学习pytorch
https://pytorch.org/tutorials/beginner/basics/intro.html

## 04pytorch实现线性回归

训练4部曲
1. 准备数据集
2. 通过神经网络设计模型
3. 构造损失函数和优化器
4. 训练

### 构造线性模型
```python
class LinearModel(torch.nn.Module):
    def __init__(self):
        super(LinearModel, self).__init__()
        self.linear = torch.nn.Linear(1,1)
    def forward(self, x):
        y_pred = self.linear(x)
        return y_pred
```

如何理解torch.nn.Linear

https://pytorch.org/docs/stable/generated/torch.nn.Linear.html

理解：y = xw + b
假设y = n x 2
x = n x 3, w = 3 x 2 即可。

从直观上更好理解。 一般将n作为第多少个样本。 列用来表示特征个数。


## 05逻辑斯蒂回归

分类问题和回归问题区别
![](https://luke-1307356219.cos.ap-chongqing.myqcloud.com//markdown/202403182236013.png)

存在一个关键。如何将实数域的值map 到[0, 1]

损失函数
![](https://luke-1307356219.cos.ap-chongqing.myqcloud.com//markdown/202403182253327.png)

对于线性回归问题来说，损失函数计算的是距离。
对于分类问题，损失函数如何理解？

利用交叉商来表示

如何理解交叉商
https://www.bilibili.com/video/BV1mZ4y1R76t/?spm_id_from=333.337.search-card.all.click&vd_source=842b1225f5d953c8df3fd60918cd05ff

理解
> 如果y_pred = y ，那么交叉商 = 信息商
> 否则， 交叉商 >= 信息商。

信息商
> https://www.bilibili.com/video/BV1Ga41127Zu/?spm_id_from=333.337.search-card.all.click&vd_source=842b1225f5d953c8df3fd60918cd05ff


## 07 加载数据集

### 为什么使用mini-batch
Batch训练数据，虽然速度快， 但是容易进入鞍点。
SGD容易走出鞍点，但是训练速度慢。

epoch = one forward pass and one backward pass of all the training examples
batch-size = the number of training data in one forward
iteration = datasize / batchsize, in one epoch, the number of train count to use batch-size to train all data

```python
for i in range(epoch):
    for i in range(iteration):
        pass

```

### dataloader

![](https://luke-1307356219.cos.ap-chongqing.myqcloud.com//markdown/202403200027418.png)

方便进行mini-batch的训练

## 08 多分类问题
### softmax
保证所有输出都大于0。
和为1。

![](https://luke-1307356219.cos.ap-chongqing.myqcloud.com//markdown/202403202049423.png)

https://victorzhou.com/blog/softmax/

a soft-max layer is to change a realtime number to probability distribution.

transform ： 归一化


## 09卷积神经网络
全连接神经网络为什么不好？

全连接神经网络（Fully Connected Neural Networks，FCNN）和卷积神经网络（Convolutional Neural Networks，CNN）都是深度学习的重要组成部分，但在许多情况下，CNN的表现优于FCNN，主要有以下几个原因：

1. 参数数量：全连接神经网络中，每个神经元都与前一层的所有神经元相连，这导致参数数量非常庞大，计算复杂度高，而且容易过拟合。而卷积神经网络通过局部感知域和权值共享大大减少了参数数量。

2. 对空间结构的处理：全连接神经网络忽略了输入数据的空间结构信息，所有的输入都被平铺成一个向量，这对于图像等具有空间结构的数据来说，会丢失大量有用信息。而卷积神经网络能够保持输入数据的空间结构，并通过卷积操作捕获局部特征。

3. 平移不变性：卷积神经网络具有平移不变性，即无论目标在图像的哪个位置，卷积操作都可以检测到。而全连接神经网络则没有这个特性。

4. 模型的泛化能力：由于卷积神经网络的参数数量少，可以有效防止过拟合，提高模型的泛化能力。

因此，在处理图像、语音等具有空间结构的数据时，卷积神经网络通常比全连接神经网络效果更好。

### 卷积核
用来提取图像特征。

直观理解。
假设一个kernel = 3x3的卷积器。
原始数据经过卷积器后，就可以提取局部特征

卷积核的意义就是去提取图像的特征
卷积核的样子是有不同的。
https://www.bilibili.com/video/BV1VV411478E/?spm_id_from=333.337.search-card.all.click&vd_source=842b1225f5d953c8df3fd60918cd05ff

### 下采样：max-pooling
用来减少数据量

### 理解
这里要明白一个点，哪些block是有参数的，哪些是没有的。
线性层，卷积层有参数。因为需要训练卷积层的参数。

卷积层对输入channel进行扩张，就是为了训练不同的卷积层，提取不同的特征。


test:
> 对一个图片经过卷积层，查看不同channel的值。

可以看到，经过训练后的卷积层，每个channel的权重值不一样。
![](https://luke-1307356219.cos.ap-chongqing.myqcloud.com//markdown/202403242153425.png)
## 10高级卷积神经网络

googleNet
### inception block
对于神经网络来说， 超参数kernelSize的选取非常难？
如何选取呢？

既然不知道哪个好，就把各种可能都尝试下， 然后累积到一起。训练完成后，效果好的配置权重就大，效果不好的权重就小。

![](https://luke-1307356219.cos.ap-chongqing.myqcloud.com//markdown/202403231753250.png)

要保证每个路径的结果W，H一致 ，要利用stride和padding

1x1的卷积有什么用？

### 如何理解信息融合

假设有3维向量，表示语文，英语，数据的成绩
```angular2html
[100, 110, 87]
[11, 109, 60]

如何比较这俩个向量呢？
最简单的算法就是将3维向量转为1维向量。然后进行比较。

这个转为1维向量的过程，就是信息融合。
```

1x1的卷积，可以将多通道的信息进行融合。本质就是将某个位置的值，sum了每个通道。

> 理解卷积核后的输出通道。 用的是相同size，但是不同权重，取出多个维度特征。

1. 提前对数据进行降低维度。减少数据量。
2. 对不同通道信息进行融合。


resNet
### 梯度消失

![](https://luke-1307356219.cos.ap-chongqing.myqcloud.com//markdown/202403242110191.png)
为啥resNet可以解决梯度消失？

### 后面的话
1. 深度学习理论
2. 多阅读Pytorch文档，至少通读一遍
3. 复现一些经典的工作
4. 扩充视野