# SeekArray Version
#
# Author: RenosGPS
# DATE  : 2024 01 29
# COORDS: 35 33
#
# old name: SEEK ARRAY
# new name: POPPANEL
#
# import
import requests
import simplejson as json

# import pendulum
from datetime import datetime, timezone, timedelta 
# 

#tz = pendulum.timezone('Europe/Athens')

tz = timezone(timedelta(hours=3))

def popPanel():
    # request data
    KINODATA = "https://api.opap.gr/draws/v3.0/1100/last-result-and-active"
    response = requests.get(KINODATA)
    if response.status_code == 200:
        json_data = response.json()
        winningNumbers = json_data['last']['winningNumbers']['list']
        drawTime = json_data['last']['drawTime']
        drawId = json_data['last']['drawId']
        winningTicket = json.loads(str(winningNumbers))
        winningTicket.sort()
    else:
        print(f"Error: {response.status_code}")
    Ticket = winningTicket
    drawTime = drawTime / 1000
    drawTime = datetime.fromtimestamp(int(drawTime))
    print("\n")
    print(f"Draw Id: {drawId}")
    print(f"Draw Time: {drawTime}")
    print("\n")
    # Make a panel array
    Panel = []
    for i in range(0,80,1):
        Panel.append("--")
    # magic to happen here
    for i in range(0,20,1):
        Ticket[i] = Ticket[i] - 1
        Panel.pop(Ticket[i])
        # ZIP is temp name for variable
        ZIP = Ticket[i] + 1
        if ZIP < 10:
            ZIP = str(ZIP)
            ZIP = "-" + ZIP
        elif ZIP > 9:
            ZIP = str(ZIP)
        Panel.insert(Ticket[i],ZIP)
    # dress the magic stuff here
    counter = 1
    for i in range(0,80,1):       
        counter = counter + 1
        print(Panel[i],sep ="", end=" ")
        if counter == 11:
            counter = 1 # reset counter
            print("\n",sep="",end="")
# entry point
if __name__ == "__main__":
    popPanel()
