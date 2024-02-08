import random
from time import sleep
print "VIBE CHECK"
print ""
sleep(1)
raw_input("[Enter Name] ")
for i in range (2):
    i=random.randint(1,2)
if i==1:
    print "you passed the vibe check!"
else:
    print "you failed the vibe check"
sleep(5)
