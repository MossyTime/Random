def Tripple(x):
          s,z=0, 0
          y=[x for x in x]
          y.reverse()
          for i in range(len(y)):
                    if "1" in y[i]:
                              z+=2**s 
                    s+=1
          return z

while 1+1==2:
          x=input("Give Binrary: ")
          z=Tripple(str(x))
          print z
