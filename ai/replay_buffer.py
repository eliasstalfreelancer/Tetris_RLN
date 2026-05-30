from collections import deque
import random

class ReplayBuffer:

    def __init__(self, max_size=10000):

        self.memory = deque(maxlen=max_size)

    def  add(
        self,
        state,
        action,
        reward,
        next_state,
        done
    ):

        self.memory.append(
            (
                state,
                action,
                reward,
                next_state,
                done
            )
        )

    def sample(self, batch_size):

        return random.sample(self.memory, batch_size)

    def size(self):

        return len(self.memory)