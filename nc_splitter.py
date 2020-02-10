#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 20:11:22 2020

@author: thirschbuechler
"""
import sys, re
import ucmd_helper as u


def spitfile(name,stuff):
        name = sanitizefilename(name)
        with open(name, "w") as myfile:
            for myline in stuff:
                myfile.write(myline)
           
def sanitizefilename(stuff):
    return re.sub('[^a-zA-Z0-9\.]', ' ', stuff)
           
 
if __name__ == '__main__': 
    vers=1.0
    print("nc-splitter V"+str(vers)+", by thirschbuechler")
    print("no cmd args supported, yet")
    
    sfx = ".nc" # suffix for outputfiles
    currenttext = []
    lastfilename = "praeamble"
    
    myfile = input("input filename? ")                
    text = open(myfile, "r")
    
    q="are you sure to overwrite any O***."+sfx+"files? I won't ask again!"
    if not u.askandreturnindex(q): # if "no"
        input("aborted, you may close now")
        sys.exit(0)
        
    longname = u.askandreturnindex("longfilenames?")
        
    

    
    for line in text:
        if line.startswith("O"):
            temp = lastfilename
            if longname:
                lastfilename = line
            else:
                lastfilename = line.split("(")[0] # get new filename
            
            spitfile(temp+sfx, currenttext) # close prev file            
            currenttext = [line] # take first line of next file with you, as list
            
        else:
            currenttext.append(line)
            
            
    spitfile(lastfilename+sfx, currenttext) # close last file
    
    input("finished without errors, you may close now")
