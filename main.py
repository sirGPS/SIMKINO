"""
KINO SIMULATOR
DOCSTRING PLACEHOLDER



"""

MODULE_IS_READ = 0

MODULE_IS_READ = MODULE_IS_READ + 1

# Project : KINO SIMULATOR
# date    : 2022 10 12
# Author  : sirGPS
# PLACE   : N 3518 E 3338 (NICOSIA NE)


# CODENAME HOT COFFEE
# DATE 2022 12 04

# main python kino draw

# use a top bottom aproach at the momment
# and slash towards a bottom to top aproach


# main kino draw


# B2T (bottom 2 top aproach acronyme)
# issue variables not changing at runtime


# clean up

import krandom
# import sector
import datetime
import random
import time
#from time import sleep
import sys
import os
import subprocess


# notes on import

# notes on random
# i need random module to be imported to able generate the random numbers

# notes on datetime
# i need datetime so I can convert UNIX time

# notes on time
# I need time module to access UNIX time and use it in RANDOM SEED


# exit the RUNTIME by using quit()

# mainmenu()

# KINO DATA

# KINO has PANEL with 80 numbers

# DRAW 'draws' 20 numbers from PANEL


# GLOBAL


# classes

class Cseed:
    """
    REMARKS  CLASS Cseed

    SEED is trasformed from variable
    to class iteration

    """
    def __init__(self, value):
        self.value = value
    value = 0
    oldvalue = 0
    newvalue = 0
    as_datetime = 0
    def __str__():
        print(self.value)

    def getseed(self):
        print(self.value)

    def getnewseed(self):
        print(self.newvalue)

    def getoldseed(self):
        print(self.oldvalue)

    def oldvalue(self):
        self.oldvalue = self.value

    def newvalue(self):
        self.value = self.newvalue

seed = Cseed(1669809600)
# Variables
now = int(time.time())
dt = datetime.datetime.fromtimestamp(now)
user_datetime = 0
unix_timestamp = 0
# space = 32
# addline = 13
# TODO: SOMETIME
# rename tarkov to kino teleprompter
tarkov = " KINO$ "
# // //////////////////////////////////////////////////////////////////////////


def main():
    """
    MAIN FUNCTION IS HERE

    """
# /////////////////////////////////////
    # $ functions are fun!
    def fake_random(xseed = 5,modulus = 10 ,increment = 5,multip = 3):
        """ PSEVDORANDOM GENERATOR """
        fake_random_isREAD = 0
        fake_random_isREAD = fake_random_isREAD + 1
        while True:
            xseed = (multip * xseed + increment) % modulus
            yield xseed
            print("FAKE_RANDOM SEED:",xseed)


    def showseed():
        # prints the seed on the screen
        # keyword is W
        # 8 16 24
        addline(8)
        addspace(8)
        print("SEED CARD")
        addline(3)
        addspace(8)
        print("SEED: ", seed.value)
        addline()
        addspace(8)
        # print the datetime from seed
        seed.as_datetime = datetime.datetime.fromtimestamp(int(seed.value))
        print("DATETIME:", seed.as_datetime)
        addline(8)
        menu()

    def addline(line_counter=1):
        # adds enter line feature
        for line_counter in range(line_counter):
            print(chr(13))
            # print('\n')
            line_counter += 1
    def addspace(space_counter=1):
        # adds space char
        for space_counter in range(space_counter):
            print(chr(32), sep='', end='')
            space_counter += 1
    def showsign():
        # KIA FUN
        print(tarkov, end=' ')
        # update time
        time_update = True
        if time_update is True:
            now = time.time()
            print('>>', end='')
        else:
            print('%%', end='')
    # clear the screen
    def cls():
        addline(25)
    # def waitkey():
        # hold execution
        # UNUSED
     #   user = input("Press any key...")
# /////////////////////////////////////
    def panel():
        # add breathing space
        # title
        # 8 16 24
        addline(8)
        addspace(8)
        print("PANEL CARD")
        addline()
        addspace(8)
        print("Seed: ", seed.value)
        addline()
        addspace(8)
        seed.as_datetime = datetime.datetime.fromtimestamp(seed.value)
        print("SEED AS DATETIME:", seed.as_datetime)
        addline(2)
        # PRINT number 1 to 80 in a rect
        # redo the rect
        # declare panel of 80 balls
        panel = ()
        panel = range(1, 81)
        # c stands for counter index
        c = 0
        addspace(8)
        # for mule that does the lifting
        for x in panel:
            # make single digits like double digits
            if (x < 10):
                addspace()
            # at number 10 to 11 add a line
            if (x == 11):
                addline()
                addspace(8)
                c = 0
            # after 10th number, add a line
            if (x > 11):
                if (c == 10):
                    addline()
                    addspace(8)
                    c = 0
            print(x, sep='', end=' ')
            x += 1
            c += 1
        addline(4)
 #       waitkey()
        menu()
# /////////////////////////////////////
# DRAW
    def draw():
        # draw list will renamed as winning_card
        """
        Notes on random
        RANDOM FUNCTION USED IS random.sample()
        """
        # 8 16 24
        addline(8)
        addspace(8)
        print("DRAW CARD ")
        # print(tarkov,end= ' ')
        addline()
        addspace(8)
        print("SEED: ", seed.value)
        addline()
        addspace(8)
        seed.as_datetime = datetime.datetime.fromtimestamp(int(seed.value))
        print("DATETIME:", seed.as_datetime)
        addline(2)
        # define draw
        # temp pool for draw in order to draw
        drawing_panel = []
        # 80 balls its kino
        # drawing_panel = range(1,81)
        for drawable_number in range(1, 81):
            drawing_panel.append(drawable_number)
        winning_card = []
        # control the seed
        random.seed(seed.value)
        # control the seed equation
        # draw = random.sample(panel,20) # RANDOM SAMPLE EQUATION IS USED HERE
        for drawed_number in range(1, 21):
            drawed_number = random.choice(drawing_panel)
            winning_card.append(drawed_number)
            drawing_panel.remove(drawed_number)
        # well sort the balls
        winning_card.sort()
        # format the winning card
        addspace(8)
        counter = 1
        for drawed_number in winning_card:
            # make single digits use 2 positions
            if drawed_number < 10:
                addspace()
            # every 10th number, go next line
            if counter == 11:
                addline()
                addspace(8)
                counter = 1
            print(drawed_number, sep=' ', end=' ')
            counter += 1
        addline(8)
#        waitkey()
        menu()
# -----------------------------------------------
    def editseed():
        """
        EDIT SEED
        Change the seed with
        a user entered seed
        TODO:
        CHANGE the datetime with
        time
        ISSUE #5
        IncompatableInput #5
        """
        addline(8)
        addspace(8)
        # put current seed to old seed var
        seed.oldseed = seed.value
        if seed.oldseed == seed.value:
            print('$')
        else:
            print('%')
        # ?set something to true
        addline()
        userseed = input("NEW SEED: ")
        # lista = []
        # userx = [' '.join(format(ord(x), 'x') for x in userx)]
        # seed.newvalue = userx[0]
        # lista.append(user)
        # ISOlate the 'numbers'
        # from the rest of ascii
        # INPUT IS BUGGY # FIX FIX FIX
        # ISSUE 5 -> CHECKS NEEDED
        # if (user > 0b00101001 or user < 0b00111010):
        #    seed.newvalue = user
        #    seed.value = seed.newvalue
        # else:
        #    seed.value = seed.oldvalue
        seed.newvalue = userseed
        seed.value = seed.newvalue
        # ?set something to true
        # Pass the seed value to timestamp
        seed.as_datetime = datetime.datetime.fromtimestamp(int(seed.value))
        addline(15)
        cls()
        homecard()
        menu()
# -----------------------------------------------
    def edittime():
        """
        EDIT the TIME
        Edits the time;
        sets input to replace the time
        with a user entered one
        Also change the seed in the same process
        //
        make when you have values already 
        to accept them
        //
        accept previews value when
        press enter
        """
        addline(8)
        addspace(8)
        print("ENTER NEW DATE AND TIME ")
        addline(8)
        addspace(8)
        newyear = int(input("new year: "))
        addspace(8)
        newmonth = int(input("new month: "))
        addspace(8)
        newday = int(input("new day: "))
        addspace(8)
        newhour = int(input("new hour: "))
        addspace(8)
        newmin = int(input("new min: "))
        new_user_datetime = datetime.datetime(
            newyear, newmonth, newday, newhour, newmin)
        addspace(8)
        addline()
        unix_timestamp = datetime.datetime.timestamp(user_datetime)
        addspace(8)
        # print(int(unix_timestamp))
        seed.value = int(unix_timestamp)
        # pass this as UNIX stamp in the seed section
        # waitkey()
        # newtime = datetime.datetime.strftime("%y %m %d %H %M")
        # qdate = newtime
        # print(qdate)
        homecard()
        menu()
# -----------------------------------------------
# draw now is disabled
# def drawnow():
# """         """
#         function drawnow does this
#         setting the value of seed to now value
#         and
#         fires up draw function
#         draw and now
#         """ """

        # set seed to now

        # NOTES
        # // I want something as a loop
        # and I miss // a lot
        # # this is matriext than //
        # but kick the foxtron on it!

        # this line not work as intended
        # seed.value = int(now)

        # draw a card
        # draw()
# -----------------------------------------------
    def homecard():
        # title
        addline(4)
        addspace(8)
        print("HOME CARD")
        addline()
        addspace(8)
        print("STATS")
        addline()
        addspace(8)
        print("seed:", end=' ')
        addspace()
        print(seed.value)
        # DATETIME print
        """
        // NOT WORKING AS intended //
        addline()
        addspace(8)
        print("DATETIME: ",end='')
        print(seed_as_datetime)
        """
        addline()
        addspace(8)
        print("Keywords you can use")
        addline()
        addspace(8)
        print("H: Homecard")
        addline()
        addspace(8)
        print("P: Panel")
        addspace(8)
        print("D: Draw")
        addline()
        addspace(8)
        print("W: Show Seed")
        addspace(8)
        print("E: Edit Seed")
        addspace(8)
        print("T: Edit Time")
        addline()
        addspace(8)
        print("Q: Quit")
        addline()
        addspace(8)
        print("R: Restart")
        addline(3)
# -----------------------------------------------
    def menu():
        # get on git
        # Add first run check
        # if firstRun is True:
        # firstRun = False
        # cls()
        ##
        # if firstRun is False:
        ##
        ##
        showsign()
        userinput = input("")
        user = userinput.lower()  # lowers the input contents
        if (user == 'x'):
            krandom.fake_print()
            krandom.fake_random()
        if (user == 'd'):
            cls()
            draw()
        if (user == 'p'):
            cls()
            panel()
        if (user == 'e'):
            cls()
            editseed()
        if (user == 'w'):
            cls()
            showseed()
        if (user == 't'):
            cls()
            edittime()
        if (user == 'h'):
            cls()
            homecard()
            menu()
        if (user == 'q'):
            quit()
        if (user == 'r'):
            print('RESTARTING...')
            subprocess.call(
                [sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
        if (user == '' or user != ''):
            cls()
            homecard()
            menu()

    cls()
    homecard()
    menu()


# -----------------------------------------------
# call main
main()  # * formely mainmenu()
