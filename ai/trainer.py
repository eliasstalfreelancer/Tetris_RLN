from engine.tetris_gym import Tetris_gym

from ai.agent import Agent

from ai.replay_buffer import ReplayBuffer

from ai.viz import Viz

from engine.game import Game

class Trainer:

    def __init__(self):

        self.env = Tetris_gym() # init gym

        state = self.env.reset() # starting state like fresh game

        self.agent = Agent(len(state))

        self.best_score = 0
        
        self.episode = 0

        self.line_progresion = 6

        self.memory = ReplayBuffer()

        self.batch_size = 32
        
        self.viz = Viz()
        self.game = Game()
        
        self.loss_history = self.viz.loss_history
        self.score_history = self.viz.score_history
        self.epsilon_history = self.viz.epsilon_history

    def run(self):

        state = self.env.reset()

        while True:

            action = self.agent.action(state)

            next_state, reward, done = self.env.step(action)

            # STORE EXPERIENCE
            self.memory.add(
                state,
                action,
                reward,
                next_state,
                done
            )

            state = next_state

            # TRAIN ONLY WHEN ENOUGH MEMORY
            if self.memory.size() > self.batch_size:

                batch = self.memory.sample(
                    self.batch_size
                )

                loss = self.agent.train(batch)

                self.loss_history.append(loss)

            self.env.render()

            if done:
                
                self.episode += 1

                if self.episode % 10 == 0:

                    self.agent.update_target_model()

                    print("TARGET MODEL UPDATED")

                score = self.env.game.score


                if score > self.best_score:

                    self.best_score = score

                    print(
                        "NEW BEST:",
                        self.best_score
                    )

                self.agent.decay_epsilon()

                state = self.env.reset()