import re

icdRegex = re.compile(r'(\d) (\d\d\d\d\d) (\d\d\d\d\d) (\d)')
bt = icdRegex.search("Bottle number is 0 83046 00013 5")

print(bt.group())
