#!/usr/bin/python3
# parse keystone.common.wsgi and return number of failed login attempt

loginfail = 0

# Open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:
    # Loop over the file
    for line in kfile:
        # Check for the fail pattern
        if "- - - - -] Authorization failed" in line:
            loginfail += 1
            sections = line.split() # Access elements by sections of list.  1st= date, 2nd= time, last = IP
            print(f"Summary of Failed Login Attempt(s):\nResult number: {loginfail}\nOccurred on: {sections[0]} at {sections[1]} from {sections[-1]}\n")

print("The number of failed login attempts is", loginfail)

s
