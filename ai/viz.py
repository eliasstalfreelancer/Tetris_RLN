import matplotlib.pyplot as plt
class Viz:
    def __init__(self):
        self.loss_history = []
        self.mean_loss_history = []

        self.score_history = []
        self.mean_score_history = []

        self.epsilon_history = []

        plt.ion()

    def update_graph(self):

        plt.clf()
        # LOSS
        plt.subplot(3,1,1)
        avg_loss = sum(self.loss_history[-100:]) / 100
        self.mean_loss_history.append(avg_loss)
        plt.plot(self.mean_loss_history)
        plt.title("mean loss")

        # SCORE
        plt.subplot(3,1,2)
        
        avg_score = sum(self.score_history[-100:]) / 100
        self.mean_score_history.append(avg_score)
        plt.plot(self.mean_score_history)
        plt.title("mean score")

        # EPSILON
        plt.subplot(3,1,3)
        plt.plot(self.epsilon_history)
        plt.title("Epsilon")

        plt.tight_layout()

        plt.pause(0.001)