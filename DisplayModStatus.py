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
                
            print (n)
            for i in mlist:
                if mlist[i][1].lower() == n.lower():
                    print (i + ": " + mlist[i][0])
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
                
            print (n)
            for i in mlist:
                if mlist[i][0].lower() == n.lower():
                    print (i + ": " + mlist[i][1])
            print ""
            print ""

    return

def ReadStatus():
    StatusF = open("{}/StatusFile.txt".format(path()),"r+")
    Status = StatusF.read()
    StatusF.close()
    return Status

Status = ReadStatus()

if settings['sorting'] == "Status":
    SortModsSL(Status)
else:
    SortModsOn(Status)



t0 = time.time()

while True:
    if time.time() - t0 > settings['refresh']:
        Status = ReadStatus()
        if settings['sorting'] == "Status":
            SortModsSL(Status)
        else:
            SortModsOn(Status)
        t0 = time.time()
        
    
