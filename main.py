'''

KINO SIMULATION DRAWING OPAP PROCESS

PROTOTYPE
DATE 2022 09 
AUTHOR GPS
COPYRIGHT GPS 2022


'''








# imports

import random
import time


# variables

seed = 0 
now = time.time()
t = now
random.seed(seed)
# --
ball = set(range(1,81)) # 1 to 80
draw = {}
draw = random.sample(ball,20)
# --
counter = 0
space = chr(20)
s = space


# functions

# newline function

def newline(x):
    for i in range(x):
        print('\n')


# addspace function

def addspace(x):
    for i in range(x):
        print(s)

#newline(64)
# panel draw 

# reset counter

def panel():
    counter = 0

    for x in ball:
        counter = counter + 1 
    
        # draw the first line
        if (x < 10):
            print(s,x,end = ' ')
        # draw the rest lines
        if (x >= 10):
            print(x,end = ' ')
        # newline after 10 items
        if (counter == 10):
            counter = 0 
            newline(1)
        


# simulate the drawing here

def drawing():

    draw.sort()
    #reset counter
    counter = 0 

    for x in draw:
        counter = counter + 1 
    
        # draw the first line
        if (x < 10):
            print(s,x, end = ' ')
        # draw the rest lines
        if (x >= 10):
            print(x,end = ' ')
        # new line after 10 items
        if (counter == 10):
            counter = 0 
            newline(1)



newline(2)
panel()
newline(2)
drawing()


    
