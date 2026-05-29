from engine.tetris_gym import Tetris_gym
from ai.agent import Agent
class Trainer:
    def __init__(self):
        self.env = Tetris_gym()
        self.state = self.env.reset()
        self.agent = Agent(len(self.state))

    def run(self):
        while True:

            action = self.agent.action(state)
            #print(action)
            next_state, reward, done = self.env.step(action)

            self.env.render()

            state = next_state

            if done:

                state = self.env.reset()
        