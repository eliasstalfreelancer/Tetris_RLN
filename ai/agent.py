from ai.model import Model
import torch
import torch.nn as nn
import torch.nn.functional as F
class Agent():
    def __init__(self,state_size):
        self.model = Model(state_size)
        
    
    def action(self,state):
        state_tensor = torch.tensor(
            state,
            dtype=torch.float32
        )

        output = self.model(state_tensor)

        action = torch.argmax(output).item()

        return action