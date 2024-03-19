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


## 06逻辑斯蒂回归

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
