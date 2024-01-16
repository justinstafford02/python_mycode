#!/usr/bin/env python3

## looping vampires

count = 0

with open("dracula.txt", "r") as dracula:
    for line in dracula:
        if "vampire" in line.lower(): #checks if vampire is present; case insensitive.
            print(line, end="")
            count +=1
print(f"There are {count} vampires in this file.")            

