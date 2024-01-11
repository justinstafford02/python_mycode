#!/usr/bin/env python3

# create a list of strings
vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]
# create a second list of strings
approved_vendors = ["cisco", "juniper", "big_ip"]

# use list comprehension to iteratate throug list and create f string
result = [
        f"The vendor is {x} {'' if x in approved_vendors else '--this is not an approved vendor!'}"
        for x in vendors
        ]
#need to unpack the list with *result and no sep between elements with sep=""
print(*result, sep="", end="\nFinished\n")

