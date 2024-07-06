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
        self.softmax = torch.nn.Softmax()

    def forward(self, x):
        x = self.activeF(self.linear1.forward(x))
        x = self.activeF(self.linear2.forward(x))
        x = self.activeF(self.linear3.forward(x))
        x = self.activeF(self.linear4.forward(x))
        x = self.activeF(self.linear5.forward(x))
        x = self.softmax(x)
        return x

class SelfAttentionModel(torch.nn.Module):
  def __init__(self, num_steps, num_channels, num_outputs, **kwargs):
    super().__init__(**kwargs)

    # Initialize components for self-attention
    #
    self.K = torch.nn.Parameter((2.0*torch.rand(num_channels, num_channels)-1.0)/num_channels**0.5) # Randomly intialize each weight uniformly from [ -1/num_channels**0.5, 1/num_channels**0.5 ]
    self.Q = torch.nn.Parameter((2.0*torch.rand(num_channels, num_channels)-1.0)/num_channels**0.5)
    self.V = torch.nn.Parameter((2.0*torch.rand(num_channels, num_channels)-1.0)/num_channels**0.5)

    self.softmax = torch.nn.Softmax(dim=1)

    # Initialize output layer
    #
    self.out = torch.nn.Linear(num_steps*num_channels, num_outputs)
  def forward(self, x):
    batch_size, num_steps, num_channels = x.shape
    # Run self attention
    #
    y = []
    for i in range(batch_size): # Process one sample at a time

      x_i = x[i,:,:] # x_i has shape of [ num_steps, num_channels ]

      x_k_i = torch.matmul(x_i, self.K) # x_k_i has shape of [ num_steps, num_channels ]
      x_q_i = torch.matmul(x_i, self.Q) # x_q_i has shape of [ num_steps, num_channels ]
      x_v_i = torch.matmul(x_i, self.V) # x_v_i has shape of [ num_steps, num_channels ]

      w_i = self.softmax(torch.matmul(x_q_i, x_k_i.T)/num_channels**0.5) # w_i has shape of [ num_steps, num_steps ]
      y_i = torch.matmul(w_i, x_v_i) # y_i has shape of [ num_steps, num_channels ]

      y.append(y_i)
    y = torch.stack(y, axis=0) # y has shape of [ batch_size, num_steps, num_channels ]

    # Flatten output
    #
    y_flat = y.reshape([ batch_size, num_steps*num_channels ]) # y_flat has shape of [ batch_size, num_steps*num_channels ]

    # Run output layer
    #
    l = self.out(y_flat) # l has shape of [ batch_size, num_outputs ]

    return l