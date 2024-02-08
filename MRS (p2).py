from time import sleep
import sys
def write(word):
          for char in word:
                    sleep(0.1)
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    

x=input("Think of a number between 1-10: ")
sleep(1)
print("accensing brainwaves...")
print("[==    ]")
sleep(2)
print("analizing memories...")
print("[====  ]")
sleep(2)
print("evaluating emotional state...")
print("[======]")
sleep(2)
print("compiling thought proccess...")
for i in range(3):
          write("[")
          write("======")
          print"]"
          
sleep(1)
print ""
print "You were thinking of the number",x
while True:
          input("")
          

