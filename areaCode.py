#!/usr/bin/python
import re
phone = "602-343-8747"
print("The area code is: " + re.match(r"^[0-9]*", phone).group())
