from engine.tetris_gym import Tetris_gym
import time
import keyboard
gym = Tetris_gym()
while True:
    state, reward, done = gym.step(3)
    
    if keyboard.read_key() == "r":
        gym.render(.5)
    if done == True:
        gym.reset()
   
