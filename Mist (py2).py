def Mist(x):
      y=[]
      z=""
      if x==0:
            z=0
      else:
            while x>=1:
                  y.append(str(x%2))
                  x/=2
            y.reverse()
            for i in range(len(y)):
                  z+=y[i]
      return z

while 1+1==2:
      x=input("Give Decimal: ")
      z=Mist(x)
      print z
