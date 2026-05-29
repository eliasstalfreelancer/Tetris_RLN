from ai.model import Model
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import random

class Agent():
    def __init__(self,state_size):
        self.model = Model(state_size)

        self.optimizer = optim.Adam(
            self.model.parameters(),
            lr=0.001
        )

        self.loss_fn = nn.MSELoss()

        self.gamma = 0.99

        self.epsilon = 1.0

        self.epsilon_decay = 0.995

        self.epsilon_min = 0.01
        
    
    def action(self, state):

        # RANDOM ACTION
        if random.random() < self.epsilon:

            return random.randint(0, 3)

        # MODEL ACTION
        state_tensor = torch.tensor(
            state,
            dtype=torch.float32
        ).unsqueeze(0)

        output = self.model(state_tensor)

        action = torch.argmax(output, dim=1).item()

        return action

    def train(self, state, action, reward, next_state, done):

            # CONVERT TO TENSORS
            state = torch.tensor(
                state,
                dtype=torch.float32
            ).unsqueeze(0)

            next_state = torch.tensor(
                next_state,
                dtype=torch.float32
            ).unsqueeze(0)

            reward = torch.tensor(
                reward,
                dtype=torch.float32
            )

            # CURRENT Q VALUES
            current_q = self.model(state)

            # NEXT Q VALUES
            next_q = self.model(next_state)

            # TARGET
            target_q = current_q.clone()

            if done:

                target_value = reward

            else:

                target_value = reward + (
                    self.gamma * torch.max(next_q)
                )

            # UPDATE TARGET FOR TAKEN ACTION
            target_q[0][action] = target_value

            # LOSS
            loss = self.loss_fn(current_q, target_q)

            # BACKPROP
            self.optimizer.zero_grad()

            loss.backward()

            self.optimizer.step()

            return loss.item()

    def decay_epsilon(self):

        if self.epsilon > self.epsilon_min:

            self.epsilon *= self.epsilon_decay