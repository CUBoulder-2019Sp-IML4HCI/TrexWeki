import gym
import gym_chrome_dino
from gym_chrome_dino.utils.wrappers import make_dino
import matplotlib.pyplot as plt
import numpy as np
from  OSC_example import OSCMessenger
import skimage.measure
from pynput.keyboard import Key, Listener
import cv2
from scipy.interpolate import interp1d

messenger = OSCMessenger()
env = gym.make('ChromeDino-v0')
env = make_dino(env, timer=True, frame_stack=False)
done = True
freq = 0
action = 0
first = []

def on_press(key):
    if Key.space==key:
        action = 1
        messenger.send_io_message(list(pooled_img.reshape(-1)),action+1.0)
    print '{0} pressed'.format(
        key) 

def on_release(key):
    action = 0
    if key == Key.esc:
        exit()

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
        first = 255-np.array(observation,np.float32).reshape(80,160)
        first = first[:,:80]
        pooled_img = skimage.measure.block_reduce(first, (6,6), np.max)
        # plt.imshow(pooled_img,interpolation="gaussian")
        # plt.show("frame.jpg")
        # print pooled_img.shape
        freq += 1
        if freq%3==0:
            messenger.send_io_message(list(pooled_img.reshape(-1)),action+1.0)
    listener.join()