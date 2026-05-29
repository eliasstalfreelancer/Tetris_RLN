from engine.tetris_gym import Tetris_gym

from ai.agent import Agent

from ai.replay_buffer import ReplayBuffer

from ai.viz import Viz


class Trainer:

    def __init__(self):

        self.env = Tetris_gym()

        state = self.env.reset()

        self.agent = Agent(len(state))

        self.best_score = 0

        self.memory = ReplayBuffer()
        
        self.viz = Viz()
        self.loss_history = self.viz.loss_history
        self.score_history = self.viz.score_history
        self.epsilon_history = self.viz.epsilon_history

    def run(self):

        state = self.env.reset()

        while True:

            action = self.agent.action(state)

            next_state, reward, done = self.env.step(action)

            # STORE EXPERIENCE
            loss = self.agent.train(
                state,
                action,
                reward,
                next_state,
                done
            )
            self.loss_history.append(loss)

            self.env.render()

            state = next_state
            
            if done:
                self.score_history.append(
                    self.env.game.score
                )

                self.epsilon_history.append(
                    self.agent.epsilon
                )
                self.viz.update_graph()
                if self.env.game.score > self.best_score:

                    self.best_score = self.env.game.score

                    print(
                        "NEW BEST:",
                        self.best_score
                    )

                self.agent.decay_epsilon()

                

                state = self.env.reset()