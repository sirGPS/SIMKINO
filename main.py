"""
KINO SIMULATOR
DOCSTRING PLACEHOLDER
"""
MODULE_IS_READ = 0
MODULE_IS_READ = MODULE_IS_READ + 1
# Project : KINO SIMULATOR
# date    : 2023 07 07
# Author  : sirGPS
# PLACE   : N 3518 E 3338 (NICOSIA NE)
# CODENAME DEEP SPACE
# DATE 2023 07 07
# main python kino draw
# use a top bottom aproach at the momment
# and slash towards a bottom to top aproach
# main kino draw
# B2T (bottom 2 top aproach acronyme)
# issue variables not changing at runtime
# clean up
# ------------------------------------------
# IMPORT
# ------------------------------------------
# 
# OP KILL PENDULUM
# Note: Remove Pendulum 
# Reason: Pendulum dependencys do not install on android
# Replace Pendulum with standard timezone reference



import krandom
import poppanel
# import sector
import secrets
import datetime
from datetime import datetime, timezone, timedelta
# p ------------
# import pendulum
# ---------------
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
# ------------------------------------------
# CLASSES
# ------------------------------------------
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
    as_datetime = ""
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
# ------------------------------------------
# VARIABLES
# ------------------------------------------
first_draw = 1067855400
seed = Cseed(first_draw) # time of first draw
# Variables
now = int(time.time())
dt = datetime.fromtimestamp(now)
# p -------------------------------------------------------
tz = timezone(timedelta(hours=3)) # Patras Local Timezone
# tz = pendulum.timezone('Europe/Athens') # Patras Local Time
# ----------------------------------------------------------
user_datetime = 0
unix_timestamp = 0
# space = 32
# addline = 13
# TODO: SOMETIME
# rename tarkov to kino teleprompter
tarkov = "~$"
# ------------------------------------------
# MAIN
# ------------------------------------------
def main():
    """
    MAIN FUNCTION IS HERE

    """
# ------------------------------------------
# FAKE RANDOM
# ------------------------------------------
    def fake_random(xseed = 1686495900,modulus = 47 ,increment = 5,multip = 3):
        """ PSEVDORANDOM GENERATOR """
        fake_random_isREAD = 0
        fake_random_isREAD = fake_random_isREAD + 1
        while True:
            xseed = (multip * xseed + increment) % modulus
            yield xseed
            print("FAKE_RANDOM SEED:",xseed)
# ------------------------------------------
# SHOW SEED
# ------------------------------------------
    def showseed():
        # prints the seed on the screen
        # keyword is W
        # 8 16 24
        addline(8)
        addspace(8)
        print("SEED CARD")
        addline(3)
        addspace(8)
        print(f"SEED: {seed.value}")
        addline()
        addspace(8)
        # print the datetime from seed
        seed.as_datetime = datetime.fromtimestamp(int(seed.value))
        # p ---------------------------------------------
        # seed.as_datetime = tz.convert(seed.as_datetime)
        # -----------------------------------------------
        print(f"DATETIME: {seed.as_datetime}")
        addline(8)
        menu()
# ------------------------------------------
# ADDLINE
# ------------------------------------------
    def addline(line_counter=1):
        # adds enter line feature
        for line_counter in range(line_counter):
            print(chr(13))
            # print('\n')
            line_counter += 1
# ------------------------------------------
# ADDSPACE
# ------------------------------------------
    def addspace(space_counter=1):
        # adds space char
        for space_counter in range(space_counter):
            print(chr(32), sep='', end='')
            space_counter += 1
# ------------------------------------------
# SHOWSIGN
# ------------------------------------------            
    def showsign():
        # KIA FUN
        print(tarkov, end=' ')
        # update time
        time_update = True
        if time_update is True:
            now = time.time()
            print('', end='')
        else:
            print('', end='')
# ------------------------------------------
# CLS
# ------------------------------------------
    # clear the screen
    def cls():
        addline()
    # def waitkey():
        # hold execution
        # UNUSED
     #   user = input("Press any key...")
# ------------------------------------------
# PANEL
# ------------------------------------------
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
        seed.as_datetime = datetime.fromtimestamp(seed.value)
        # p --------------------------------------------
        # seed.as_datetime = tz.convert(seed.as_datetime)
        # ----------------------------------------------
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
# ------------------------------------------
# DRAW
# ------------------------------------------
    def draw2():
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
        seed.as_datetime = datetime.fromtimestamp(int(seed.value))
        # p ---------------------------------------------
        # seed.as_datetime = tz.convert(seed.as_datetime)
        # ------------------------------------------------
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

    def draw():
        # function added on 2024 02 08 15:37
        addline(8)
        addspace(8)
        print("Draw ""Winning"" Card")
        addline()
        addspace(8)
        print(f"Seed is:{seed.value}")
        addline()
        addspace(8)
        seed.as_datetime = datetime.fromtimestamp(int(seed.value))
        # p --------------------------------------------
        # seed.as_datetime = tz.convert(seed.as_datetime)
        # ----------------------------------------------
        print(f"Datetime is:{seed.as_datetime}")
        addline(2)

        # draw the winning ticket
        drawing_pool = []
        for drawable_number in range(1,81,1):
            drawing_pool.append(drawable_number)
        ticket = []
        random.seed(seed.value)
        for drawed_number in range(1,21,1):
            drawed_number = random.choice(drawing_pool)
            ticket.append(drawed_number)
            drawing_pool.remove(drawed_number)
        ticket.sort()
        # make my panel
        panel = []
        for i in range (0,80,1):
            panel.append("--")
        # magic
        for i in range(0,20,1):
            ticket[i] = ticket[i] - 1
            panel.pop(ticket[i])
            ZIP = ticket[i] + 1
            if ZIP < 10:
                ZIP = str(ZIP)
                ZIP = "-" + ZIP
            elif ZIP > 9:
                ZIP = str(ZIP)
            panel.insert(ticket[i],ZIP)
        # dress the magic
        counter = 1
        for i in range(0,80,1):
            counter = counter + 1
            print(panel[i],sep="",end=" ")
            if counter == 11:
                counter = 1
                print("\n",sep="",end="")

        

        addline()
        menu()


# ------------------------------------------
# EDIT SEED
# ------------------------------------------
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
            print('')
        else:
            print('')
        # ?set something to true
        addline()
        addspace(8)
        print(f"Current Seed: {seed.value}")
        addspace(8)
        print("ENTER NEW SEED")
        addline(4)
        addspace(8)
        userseed = input("NEW SEED: ")
        if userseed == 'first draw':
            userseed = first_draw
        seed.value = userseed
        seed.newseed = seed.value
        seed.as_datetime = datetime.fromtimestamp(int(seed.value))
        # p -------------------------------------------
        # seed.as_datetime = tz.convert(seed.as_datetime)
        # ---------------------------------------------
        addline(4)
        addspace(8)
        print(f"New Current Seed: {seed.value} ")
        addspace(8)
        print("DATETIME:", seed.as_datetime)
        addline(2)
        addspace(8)
        prompt = input("Return...")
        addline(15)
        cls()
        homecard()
        menu()
# ------------------------------------------
# EDIT TIME
# ------------------------------------------
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

        #revamb needed

        # datetime get
        old_datetime = time.time()
        old_datetime = datetime.fromtimestamp(old_datetime)
        #print("OLD_DATETIME: ",old_datetime)
        #print("\nOLD_MINUTE:", old_datetime.minute)
        #
        #datetime()

        oldyear = old_datetime.year
        oldmonth = old_datetime.month
        oldday = old_datetime.day
        oldhour = old_datetime.hour
        oldmin = old_datetime.minute

        # do finish with intervals of 5 minutes
        addline(8)
        addspace(8)
        print("ENTER NEW DATE AND TIME ")
        addline(8)
        addspace(8)
        try:
            newyear = int(input(f"new year ({oldyear}): "))
        except:
            newyear = int(oldyear)
        addspace(8)
        try:
            newmonth = int(input(f"new month ({oldmonth}): "))
        except:
            newmonth = int(oldmonth)
        addspace(8)
        try:
            newday = int(input(f"new day ({oldday}): "))
        except:
            newday = int(oldday)
        addspace(8)
        try:
            newhour = int(input(f"new hour ({oldhour}): "))
        except:
            newhour = int(oldhour)
        addspace(8)
        try:
            newmin = int(input(f"new min ({oldmin}):  "))

        except:
            newmin = int(oldmin)


            if newmin < 55:
                if newmin / 5 == range(0,11):
                    newmin = (abs(int(newmin))*5)
                else:
                    newmin = (abs(int(newmin/5))*5)
            elif newmin > 55:
                    # todo: shift to 55 min
                newmin = 55

                newmin = int(newmin)
                


        if newmin > 55:
            newmin = 55
            

        new_user_datetime = datetime(
            newyear, newmonth, newday, newhour, newmin)
        user_datetime = datetime.timestamp(new_user_datetime)
        addspace(8)
        addline()
        unix_timestamp = datetime.timestamp(new_user_datetime)
        addspace(8)


        # print(int(unix_timestamp))


        seed.value = int(unix_timestamp)


        # pass this as UNIX stamp in the seed section
        # waitkey()
        # newtime = datetime.strftime("%y %m %d %H %M")
        # qdate = newtime
        # print(qdate)


        homecard()
        menu()

# ------------------------------------------
# DRAW-NOW DEFUCT
# ------------------------------------------
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


# ------------------------------------------
# HOMECARD
# ------------------------------------------
    def homecard():
        """
        Dress of the menu system
        """
        # title
        addline(4)
        addspace(8)
        print("HOME CARD")
        addline()
        addspace(8)
        print("STATS")
        addline()
        addspace(8)
        print(f"seed: {seed.value}", end=' ')
        addline()
        addspace(8)
        seed.as_datetime = datetime.fromtimestamp(int(seed.value))
        # p ---------------------------------------------
        # seed.as_datetime = tz.convert(seed.as_datetime)
        # -----------------------------------------------
        print(f"Datetime: {seed.as_datetime}")

        
     
  
        addline(2)
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
        addline()
        addspace(8)
        print("X: SECRET RANDOM FUNCTION")
        addline()
        addspace(8)
        print("F: Show Last and Active KINO Draw")
        addline(3)
        
# ------------------------------------------
# MENU
# ------------------------------------------
    def menu():
        """
        Logic to the menu system

        """      
        showsign()
        userinput = input("")
        user = userinput.lower()  # lowers the input contents
        if (user == 'x'):
            cls()
            print("SECRET RANDOM FUNCTION TEST")
            addline(3)
            #krandom.fake_print()
            addline(2)
            krandom.fake_random()
            addline(2)
            #krandom.fake_fortuna()
            addline(8)
            menu()
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
        if (user == 'f'):
            cls()
            print("KINO: Last Draw and Active Draw")
            addline()
            poppanel.popPanel()
            addline()
            menu()
            #prompt = input("") # press any key..
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
    #cls()
    #homecard()
    menu()


# ------------------------------------------
# MAIN
# ------------------------------------------
# call main
# * formely mainmenu()

# entry point
if __name__ == "__main__":
    main()
