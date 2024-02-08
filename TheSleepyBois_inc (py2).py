import sys
from time import sleep
def t1(words):
    for char in words:
        sleep(0.1)
        sys.stdout.write(char)
def t2(words):
    for char in words:
        sleep(0.2)
        sys.stdout.write(char)
def t3(words):
    for char in words:
        sleep(0.01)
        sys.stdout.write(char)
print "This",
sleep(1)
print "is"
sleep(0.5)
t1("=======")
t3("-_-_-_-_-_-_-_-_-_-")
sleep(0.5)
print "The",
sleep(0.5)
print "Sleepy",
sleep(0.5),
print "Bois",
sleep(0.5)
t1(".inc")
sleep(0.5)
t3("-_-_-_-_-_-_-_-_-_-")
c=0
print ""
while c==0:
    t1("\nSelect Chapter:")
    sleep(1)
    print""
    print "1.Crow"
    sleep(1)
    print "2.Pig"
    sleep(1)
    print "3.Ghost"
    sleep(1)
    print "4.Chicken"
    sleep(1)
    c=raw_input("[1,2,3,4]")
    print ""
    if c!="i dont do lyrics":
        while c=="1":
            t1("Chapter 1\n=========")
            t2("\nPhil")
            sleep(2)
            print "\nName: ",
            sleep(1)
            t1("Philza Minecraft")
            sleep(2)
            print "\nAge: ",
            sleep(1)
            t1("Quite old")
            sleep(2)
            print "\nMarried: ",
            sleep(1)
            t1("Woman")
            sleep(2)
            print "\nThat is: ",
            sleep(1)
            t1("Interesting")
            print""
            sleep(2)
            c=0
        while c=="2":
            t1("Chapter 2\n=========")
            t2("\nTechnoblade")
            sleep(2)
            print "\nHe has: ",
            sleep(1)
            t1("A golden crown")
            sleep(2)
            print "\nHe wears: ",
            sleep(1)
            t1("A gown")
            sleep(2)
            print "\nIn the gown: ",
            sleep(1)
            t1("He doesnt own knives")
            print""
            sleep(2)
            c=0
        while c=="3":
            t1("Chapter 3\n=========")
            t2("\nWilbur")
            sleep(2)
            print "\nHe is: ",
            sleep(1)
            t1("A musician")
            sleep(2)
            print "\nHe sings about: ",
            sleep(1)
            t1("Women")
            sleep(2)
            print "\nI find it: ",
            sleep(1)
            t1("Cool")
            print""
            sleep(2)
            c=0
        while c=="4":
            t1("Chapter 4\n=========")
            t2("\nTommy")
            sleep(2)
            print "\nHe is: ",
            sleep(1)
            t1("Massive")
            sleep(2)
            print "\nHe is: ",
            sleep(1)
            t1("Massive")
            print ""
            sleep(2)
            c=0
    else:
        print "*banned*"
        sleep(2)
