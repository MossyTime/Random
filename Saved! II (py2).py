f=0                 
L1=[]
L2=[]
L3=[]
L=[0,0,0]
LN=["(empty)","(empty)","(empty)"]
h=0
n=0
print " Saved! II"
print "========"
b="back"
enter=raw_input("[enter, exit] ")
while enter not in ["enter","exit"]:
          enter=raw_input("[enter, exit] ")
if enter=="enter":
          pass
elif enter=="exit":
          exit()
while b=="back":
          while f==0:
                    while L==[0,0,0]:
                              print "no libraries. create new library"
                              s=input("select library slot: [1,2,3] ")
                              n=raw_input("Name your library: ")
                              LN[s-1]=n
                              L[s-1]="L"+str(s)
                              print n,"created in slot",s
                              f=1
                              b="back"
          print ""
          print "Libraries:",LN
          b=raw_input("[new / delete / exit] or library name ")
          if b=="exit":
                    ex=raw_input("Are you sure you want to exit? All libraries will be deleted: [confirm / cancel] ")
                    while ex not in ["confirm","cancel"]:
                              ex=raw_input("Are you sure you want to exit? All libraries will be deleted: [confirm / cancel] ")
                    if ex=="confirm":
                              exit()
                    elif ex=="cancel":
                              pass
          while b=="new":
                    print ""
                    s=input("Select library slot: [1,2,3] ")
                    slot="L"+str(s)
                    if slot in L:
                              print LN[s-1],"already exists in this slot"
                    else:
                              n=raw_input("Name your library: ")
                              if n in LN:
                                        print "Name already in use"
                              else:
                                       LN[s-1]=n
                                       L[s-1]="L"+str(s)
                                       print slot,"created, in slot",s
                              b="back"
          while b=="delete":
                    print ""
                    print LN
                    s=raw_input("Delete library: ")
                    if s in LN:
                              slot="L"+str(LN.index(s)+1)
                              print "deleted",s,"from slot",LN.index(s)+1
                              L[LN.index(s)]=0
                              del eval("L"+str(LN.index(s)+1))[:]
                              LN[LN.index(s)]="(empty)"        
                    if L==[0,0,0]:
                              f=0
                    b="back"
          while b in LN and h!="back":
                    if b in LN and h!="back":
                              print ""
                              print b
                              print "="*len(b)
                              print eval("L"+str(LN.index(b)+1))
                              h=raw_input("[add / remove / back] ")
                              li=eval(L[LN.index(b)])
                              while h=="add":
                                        print ""
                                        added=raw_input("Add to library: ")
                                        li.append(added)
                                        print "added",added,"to",b
                                        h=0
                              while h=="remove":
                                        print eval("L"+str(LN.index(b)+1))
                                        removed=raw_input("Remove from library: ")
                                        try:
                                                  li.remove(removed)
                                                  print "removed",removed,"from",b
                                        except ValueError:
                                                  print removed,"not in library"
                                        h=0
                    else:
                              print ""
                              print "Library doesnt exist"
                              h="back"
          h=0
          b="back"
                              
                              
                              
                    
                    
                              
                              

