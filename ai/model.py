
import torch
import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):

    def __init__(self,input): # model

        super().__init__()

        self.fc1 = nn.Linear(input, 128)

        self.fc2 = nn.Linear(128, 128)

        self.output = nn.Linear(128, 4)

    def forward(self, x): #predict 

        x = F.relu(self.fc1(x))

        x = F.relu(self.fc2(x))

        x = self.output(x)

        return x 

