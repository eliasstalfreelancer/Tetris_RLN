import matplotlib.pyplot as plt
class Viz:
    def __init__(self):
        self.loss_history = []

        self.score_history = []

        self.epsilon_history = []

        plt.ion()
        
    def update_graph(self):

        plt.clf()

        # LOSS
        plt.subplot(3,1,1)
        plt.plot(self.loss_history)
        plt.title("Loss")

        # SCORE
        plt.subplot(3,1,2)
        plt.plot(self.score_history)
        plt.title("Score")

        # EPSILON
        plt.subplot(3,1,3)
        plt.plot(self.epsilon_history)
        plt.title("Epsilon")

        plt.tight_layout()

        plt.pause(0.001)