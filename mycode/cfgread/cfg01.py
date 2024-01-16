#!/usr/bin/env python3

def main():
    ## create file object in "r"ead mode
    configfile = open("vlanconfig.cfg", "r")
    
    # display file to screen with .read()
    configblog = configlist.read()

    ## strip out \n 
    configlist = configblog.splitlines()

    print(configlist)

    ## Always close your file
    configfile.close()



