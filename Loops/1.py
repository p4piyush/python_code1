inn=5

for i in range (0,inn):
    print("")
    for j in range (inn-i,0,-1):
        print(" ",end="")
    for k in range (0,i+1):
        print("|",end=" ");


for i in range (0,inn):
    print(""*(inn-i-1))
    print(" "*(inn-i),end=" ")
    print("*"*(i+1),end=" ")
    
