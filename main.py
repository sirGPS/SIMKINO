# Project : KINO SIMULATOR
# date    : 2022 10 12
# Author  : sirGPS
# PLACE   : N 3518 E 3338 (NICOSIA NE)





# CODENAME USERINPUT SHARP
# DATE 2022 11 03

#main python kino draw

# use a top bottom aproach at the momment
# and slash towards a bottom to top aproach



#main kino draw


#B2T (bottom 2 top aproach acronyme)
# issue variables not changing at runtime


# clean up 



#import sector

import random
import datetime
import time
from time import sleep





#notes on import

#notes on random
# i need random module to be imported to able generate the random numbers

#notes on datetime
# i need datetime so I can convert UNIX time

#notes on time
# I need time module to access UNIX time and use it in RANDOM SEED



# exit the RUNTIME by using quit()

#mainmenu()

# KINO DATA

# KINO has PANEL with 80 numbers

# DRAW 'draws' 20 numbers from PANEL


#GLOBAL




class Cseed:
    """
    // REMARKS  CLASS Cseed

    // SEED is trasformed from variable
    // to class iteration

    """

    def __init__(me,value):
        me.value = value
        
    value = 0

    def __str__():
        print(me.value)
    

    def getseed():
        print(me.value)

    
seed = Cseed(11)



now = int(time.time())
dt = datetime.datetime.fromtimestamp(now)
seed_as_datetime = datetime.datetime.fromtimestamp(seed.value)


space = 32
addline = 13

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

    
    def showseed():
        # 8 16 24
        addline(8)
        #print(tarkov,end= ' ')
        addspace(8)
        print("SEED CARD")
        addline()
        addspace(8)
        print("SEED: ",seed.value)
        addline()
        addspace(8)
        seed_as_datetime = datetime.datetime.fromtimestamp(seed.value)
        print("SEED AS DATETIME:",seed_as_datetime)
        addline()
        
        
        #waitkey()
        menu()
        
    

    def addline(x = 1):
        for x in range(x):
            print(chr(13))
            #print('\n')
            x = x + 1
            
        
    def addspace(x = 1):
        for x in range(x):
            print(chr(32),sep = '',end = '' )
            x = x + 1

    def showsign():
        print(tarkov,end= ' ')

    # clear the screen
    def cls():
        addline(25)
    
    def waitkey():
        # hold execution
        user = input("Press any key...")
        
        
# /////////////////////////////////////
        

    def panel():

        # add breathing space


        #title
        # 8 16 24        
        addline(8)
        addspace(8)
        print("PANEL CARD")
        addline()
        addspace(8)
        print("Seed: ",seed.value)
        addline()
        addspace(8)
        seed_as_datetime = datetime.datetime.fromtimestamp(seed.value)
        print("SEED AS DATETIME:",seed_as_datetime)

        addline(2)
        # PRINT number 1 to 80 in a rect

        #redo the rect

        # declare panel of 80 balls
        panel = ()
        panel = range(1,81)
        # c stands for counter index
        c = 0

        # for mule that does the lifting 
        for x in panel:
            # make single digits like double digits
            if (x < 10):
                addspace()
            # at number 10 to 11 add a line
            if (x == 11):
                addline()
                c = 0
            # after 10th number, add a line    
            if (x > 11):    
                if (c == 10):
                    addline()
                    c = 0    
            print(x,sep = '',end=' ')
            x = x + 1
            c = c + 1
            
            
        addline(4)
 #       waitkey()
        menu()


# /////////////////////////////////////

    def draw():
        
        """
        Notes on random
        
        RANDOM FUNCTION USED IS random.sample()
        
        """
        

        # 8 16 24
        
        addline(8)
        addspace(8)
        print("DRAW CARD ")
        #print(tarkov,end= ' ')
        addline()
        addspace(8)
        print("SEED: ",seed.value)
        addline()
        addspace(8)
        seed_as_datetime = datetime.datetime.fromtimestamp(seed.value)
        print("DATETIME:",seed_as_datetime)
        addline(2)

        #define draw

        # temp pool for draw in order to draw
        panel = ()
        # 80 balls its kino
        panel = range(1,81)

        
        draw = []
        # control the seed
        random.seed(seed.value)
        # control the seed equation
        draw = random.sample(panel,20) # RANDOM SAMPLE EQUATION IS USED HERE
        # well sort the balls
        draw.sort()


        c = 1
        for x in draw:

            # make single digits use 2 positions 
            if x < 10:
                addspace()

            # every 10th number, go next line
            if c == 11:
                addline()
                c = 1
                
            print(x,sep = ' ', end = ' ')
            c = c + 1

                

        
        addline(8)
#        waitkey()
        menu()


# /////////////////////////////////////        

    def editseed():
        
        """
        EDIT SEED
        
        Change the seed with
        a user entered seed
        
        TODO:
        CHANGE the datetime with
        time
        
        
        """
        
        addline(8)
        #print(tarkov,end= ' ')
        addspace(8)
        newseed = int(input("NEW SEED: "))
        seed.value = newseed
        showseed()
        # print("NEW SEED IS: ", seed)
        addline(15)
#        waitkey()
        
        homecard()
        menu()
        
        
    def edittime():
        
        
        """
        EDIT the TIME
        
        Edits the time;
        sets input to replace the time
        with a user entered one
        
        Also change the seed in the same process
        
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
        
        global user_datetime
        
        user_datetime = datetime.datetime(newyear,newmonth,newday,newhour,newmin)
        
        addspace(8)
        #print(user_datetime)
        addline()
        
        unix_timestamp = datetime.datetime.timestamp(user_datetime)
        
        addspace(8)
        #print(int(unix_timestamp))
        seed.value = int(unix_timestamp)
        # pass this as UNIX stamp in the seed section
        
        #waitkey()
        # newtime = datetime.datetime.strftime("%y %m %d %H %M")
        # qdate = newtime
        # print(qdate)
        
        
        homecard()
        menu()
        
        

# /////////////////////////////////////


    # draw now is disabled
    #def drawnow():

        """

        function drawnow does this

        setting the value of seed to now value
        and
        fires up draw function

        draw and now


        """

        
        # set seed to now
        
        # NOTES        
        # // I want something as a loop
        # and I miss // a lot
        # # this is matriext than //
        # but kick the foxtron on it!


        # this line not work as intended        
        # seed.value = int(now)
        
        
        # draw a card
        #draw()
        
        
        
# /////////////////////////////////////////////////////////

    def homecard():
        
        #title
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
        print("S: Show Seed")
        addspace(8)
        print("E: Edit Seed")
        addspace(8)
        print("T: Edit Time")
                
        addline()
        addspace(8)
        print("Q: Quit")
        
        addline(3)
        
        
# /////////////////////////////////////////////////////////

    def menu():
        
        
        # get on git      
        

        #Add first run check


        
##        if firstRun is True:
##            firstRun = False
##            cls()
##
##        if firstRun is False:
##                
##        

        showsign()
        userinput = input("")
        user = userinput.lower() # lowers the input contents

        if (user == 'd'):
            cls()
            draw()

        if (user == 'p'):    
            cls()
            panel()

        if (user == 'e'):
            cls()
            editseed()
            
        if (user == 's'):
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
        
        if (user == '' or user != ''):
            cls()
            homecard()
            menu()
        
        
        

        
    
    

    cls()
    
    homecard()
    menu()


# /////////////////////////////////////////////////////////////////////////////


#call main
    
main() # * formely mainmenu()













