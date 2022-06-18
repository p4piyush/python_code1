def inside():
    print ("inside")
    def outside():
        print("outside")

x= inside()
print(x)