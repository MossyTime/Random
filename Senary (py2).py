def Hex(x):
          L=[0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
          y=[x for x in x]
          y.reverse()
          z,h="",""
          for q in range(len(y)//4):
                    g,f=0,0
                    for i in range(4):
                              f+=int(y[0])*2**g
                              del y[0]
                              g+=1
                    z+=str(L[f])
          p=[z for z in z]
          p.reverse()
          for char in range(len(p)):
                    h+=p[char]
          print(h)
          
while 1==1:
          x=input("Give Binrary: ")
          Hex(x)

