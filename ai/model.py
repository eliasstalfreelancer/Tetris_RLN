
import torch
import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):

    def __init__(self,input): # model

        super().__init__()

        self.fc1 = nn.Linear(input, 128) # input layers

        self.fc2 = nn.Linear(128, 128)  #hidden layer

        self.output = nn.Linear(128, 4) #output layer

    def forward(self, x): #predict 

        x = F.relu(self.fc1(x)) #activation layer

        x = F.relu(self.fc2(x)) # activation layer

        x = self.output(x) #output layer

        return x 

