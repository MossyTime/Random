import sys
from time import sleep
ink=20
print "======="
words = "PRINTER"
for char in words:
    sleep(0.2)
    sys.stdout.write(char)
print ""
print "======="
x=raw_input("what? ")
while x!="stop":
    while x!="ink" and x!="paper" and x!="stop":
        x=raw_input("wym ")
    if x=="ink":
        ink=20
        print "ink full"
    elif x=="paper":
        if ink==0:
            print "no ink "
        else:    
            print "*printed paper*"
            ink-=5
    if x!="stop":
        if ink!=0:
            x=raw_input("what? ")
        else:
            x=raw_input ("give ink ")
    
