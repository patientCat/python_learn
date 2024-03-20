import torch

"""
1输入1输出网络，玩具模型
"""


class LinearModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(28 * 28, 512)
        self.linear2 = torch.nn.Linear(512, 256)
        self.linear3 = torch.nn.Linear(256, 128)
        self.linear4 = torch.nn.Linear(128, 64)
        self.linear5 = torch.nn.Linear(64, 10)
        self.activeF = torch.nn.functional.relu

    def forward(self, x):
        x = self.activeF(self.linear1.forward(x))
        x = self.activeF(self.linear2.forward(x))
        x = self.activeF(self.linear3.forward(x))
        x = self.activeF(self.linear4.forward(x))
        x = self.activeF(self.linear5.forward(x))
        return x
