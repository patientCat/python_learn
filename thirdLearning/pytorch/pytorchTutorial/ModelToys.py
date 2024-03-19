import torch

"""
1输入1输出网络，玩具模型
"""


class LinearModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1, dtype=torch.double)

    def forward(self, x):
        y_pred = self.linear.forward(x)
        return y_pred
