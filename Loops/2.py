
lst1=["Sam", "", "Ben", "Olivia", "Alicia"]

new_lst=[]

#Type your answer here.    

def name_adder(list):
    i=0
    while i<len(lst1):
        if(lst1[i]==""):
            print("There is an empty string")
            break
        elif (lst1[i]!=""):
            new_lst.append(lst1[i])
        i=i+1
        return new_lst

print(name_adder(lst1))
