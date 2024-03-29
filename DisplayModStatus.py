import clr, sys, json, os, codecs
import time
import winsound
from ast import literal_eval
import random
import re
import datetime
from datetime import datetime, timedelta

def path(): # Get path of file
    path = os.path.dirname(os.path.abspath(__file__))
    return path


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

   
try:
    settingsf = open("{}/settings.json".format(path()),"r+")
    settingsr = settingsf.read()
    settingsf.close()
    settingsr = settingsr.split("{",1)
    sr = "{" + settingsr[1]
    sr = sr.replace("  ","")
    sr = sr.replace("\n","")
    sr = sr.replace("\r","")
    sr = sr.replace("false","False")
    sr = sr.replace("true","True")
    #sr = sr.replace("\"","'")
    settings = literal_eval(sr)
except:
    settings = {"OnlyLive": False,
  "Command": "!mods",
  "REdit": "edit",
  "refresh": 10,
  "StatusList": "Available,Lurk,AudioOnly,ChatOnly,Sleep,AFK,NoStatus,Offline",
  "WrongStatusMsg": "Please choose one of the following: ",
  "GetStatus": "status",
  "sorting": "Status",
  "DefaultStatus": "NoStatus"
    }


SL = ["Available","Lurk","AudioOnly","ChatOnly", "Sleep", "AFK", "NoStatus", "Offline"]
SL = settings['StatusList']
SL = SL.strip()
SL = SL.split(",")

Actv = ['Active','Inactive','Offline']


def SortModsSL(modlist):
    os.system('cls')

        

    mlist = literal_eval(modlist)
    for n in SL:
        c = 0
        for i in mlist:
            if mlist[i][1].lower() == n.lower():
                c = c + 1
        if c > 0:
                
            print color.RED + (n) + color.END
            for i in mlist:
                if mlist[i][1].lower() == n.lower():
                    print (i + "\t(" + mlist[i][0]  + ")")
            print ""
            print ""

    return

def SortModsOn(modlist):
    os.system('cls')

        

    mlist = literal_eval(modlist)
    for n in Actv:
        c = 0
        for i in mlist:
            if mlist[i][0].lower() == n.lower():
                c = c + 1
        if c > 0:
                
            print color.RED + (n) + color.END
            for i in mlist:
                if mlist[i][0].lower() == n.lower():
                    print (i + "\t(" + mlist[i][1] + ")")
            print ""
            print ""

    return

def ReadStatus():
    StatusF = open("{}/StatusFile.txt".format(path()),"r+")
    Status = StatusF.read()
    StatusF.close()
    return Status






while True:

    Status = ReadStatus()
    if settings['sorting'] == "Status":
        SortModsSL(Status)
    else:
        SortModsOn(Status)
    time.sleep(settings['refresh'])
        
    
