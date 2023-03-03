import re
def n(mObject):
    return mObject.group("g1")+ "_" + mObject.group("g2").lower()

x = "mySuperVar" 
pattern = "(?P<g1>[a-z])(?P<g2>[A-Z])+"
print(re.sub(pattern, n, x))