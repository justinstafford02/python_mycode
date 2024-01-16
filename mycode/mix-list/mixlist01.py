#!/usr/bin/env python3
import re

iplist = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

# use for-loop to iterate through list.  use REGEX and pull out valid IP address
# in later versions of this I will use isinstance(ip, str), instead of type(ip)
# but because we've covered 'type' today, I wanted to check using 'type'
# this is the only REGEX I have ever memorized. it goes great  with beautifulsoup.
for ip in iplist:
    if type(ip) == str and re.match(r'^(\d{1,3}\.){3}\d{1,3}$', ip):
        print(ip)

exit()

