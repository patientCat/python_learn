import torch

"""
1输入1输出网络，玩具模型
"""


class CnnModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        # input channel, outputcahnnel,
        self.conv1 = torch.nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = torch.nn.Conv2d(10, 20, kernel_size=5)
        # 可以复用，没有参数
        self.pooling = torch.nn.MaxPool2d(3)
        self.linear5 = torch.nn.Linear(320, 10)
        self.activeF = torch.nn.functional.relu

    def forward(self, x):
        batchSize = x.shape[0]
        x = self.activeF(self.pooling(self.conv1(x)))
        x = self.activeF(self.pooling(self.conv2(x)))
        x = x.view(batchSize, -1)
        x = self.linear5(x)
        return x
