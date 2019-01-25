#!/usr/bin/env python3
from OSC import OSCServer
import sys
from time import sleep
from pynput.keyboard import Key, Controller

server = OSCServer( ("localhost", 12000) )
server.timeout = 0
run = True
keyboard = Controller()
# this method of reporting timeouts only works by convention
# that before calling handle_request() field .timed_out is 
# set to False
def handle_timeout(self):
    self.timed_out = True

# funny python's way to add a method to an instance of a class
import types
server.handle_timeout = types.MethodType(handle_timeout, server)

def user_callback(path, tags, args, source):
    # which user will be determined by path:
    # we just throw away all slashes and join together what's left

    # tags will contain 'fff'
    # args is a OSCMessage with data
    # source is where the message came from (in case you need to reply)
    if int(args[0]) == 2 : #jump
        keyboard.press(" ")
        sleep(0.12)
        keyboard.release(" ")
        print ("Received data from ", path,int(args[0])) 

def user_prob(path, tags, args, source):
    print ("Received data from ", path,int(args[0])) 


def quit_callback(path, tags, args, source):
    # don't do this at home (or it'll quit blender)
    global run
    run = False

server.addMsgHandler( "/wek/outputs", user_callback )
server.addMsgHandler( "/outputs-1", user_prob )

# user script that's called by the game engine every frame
def each_frame():
    # clear timed_out flag
    server.timed_out = False
    # handle all pending requests then return
    while not server.timed_out:
        server.handle_request()

# simulate a "game engine"
while run:
    # do the game stuff:
    sleep(1)
    # call user script
    each_frame()

server.close()
