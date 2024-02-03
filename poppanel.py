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
# 
def popPanel():
    # request data
    KINODATA = "https://api.opap.gr/draws/v3.0/1100/last-result-and-active"
    response = requests.get(KINODATA)
    if response.status_code == 200:
        json_data = response.json()
        winningNumbers = json_data['last']['winningNumbers']['list']
        winningTicket = json.loads(str(winningNumbers))
        winningTicket.sort()
    else:
        print(f"Error: {response.status_code}")
    Ticket = winningTicket
    
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
    c = 1
    for i in range(0,80,1):       
        c = c + 1
        print(Panel[i],sep ="", end=" ")
        if c == 11:
            c = 1
            print("\n",sep="",end="")
# entry point
if __name__ == "__main__":
    popPanel()
