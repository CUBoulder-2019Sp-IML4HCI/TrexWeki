import gym
import gym_chrome_dino
from gym_chrome_dino.utils.wrappers import make_dino
import matplotlib.pyplot as plt
import numpy as np
from  OSC_example import OSCMessenger
import skimage.measure

messenger = OSCMessenger()
env = gym.make('ChromeDino-v0')
env = make_dino(env, timer=True, frame_stack=False)
done = True
freq = 0
action = 0
first = []

from pynput.keyboard import Key, Listener

def on_press(key):
    if Key.space==key:
        action = 1
        messenger.send_io_message(first.reshape(-1),action+1)
    print '{0} pressed'.format(
        key) 

def on_release(key):
    action = 0
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    while True:
        score = env.unwrapped.game.get_score()
        if done:
            print "Done Score",score
            env.reset()
        observation, reward, done, info = env.step(action)
        first = np.array(observation).reshape(80,160)
        pooled_img = skimage.measure.block_reduce(first, (20,20), np.max)
        freq+=1
        print action,type(action)
        if freq%5==0:
            messenger.send_io_message(first.reshape(-1)[0],action+1)
    listener.join()