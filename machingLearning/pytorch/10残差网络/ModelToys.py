import torch

"""
1输入1输出网络，玩具模型
"""


class Net(torch.nn.Module):
    def __init__(self):
        super().__init__()
        """
        这里要明白一个点，哪些block是有参数的，哪些是没有的。
        线性层，卷积层有参数。因为需要训练卷积层的参数。
        
        卷积层对输入channel进行扩张，就是为了训练不同的卷积层，提取不同的特征。
        """
        # input channel, outputcahnnel,
        self.resBlock1 = ResModel()
        self.resBlock2 = ResModel()
        # 池化，可以复用，没有参数
        self.pooling = torch.nn.MaxPool2d(3)
        self.linear5 = torch.nn.Linear(20, 10)
        self.activeF = torch.nn.functional.relu

    def forward(self, x):
        batchSize = x.shape[0]
        x = self.resBlock1(x)
        x = self.resBlock2(x)
        print(f"res={x.shape}")
        x = x.view(batchSize, -1)
        x = self.linear5(x)
        return x


class ResModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 1, kernel_size=3)
        self.conv2 = torch.nn.Conv2d(1, 1, kernel_size=3)
        self.relu = torch.nn.functional.relu

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        return torch.nn.ReLU(0.5 * x + x)
