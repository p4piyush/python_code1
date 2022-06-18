

eml=input("Enter your email id:")

    
if eml.count('@')==0:   #This will check for absense of  @ symbol
    print("Enter valid email ID '@' symbol missing")

elif eml.count('@')>=2: #This will check for multiple occurances of @ symbol
    print("Enter valid email ID \nMultiple '@' symbol used in email ID")

elif eml.index('@')==0: #This will check for @ syambol at the begining of the ID
    print("Invalid Email ID plese enter valid ID...")

elif eml.index('@')>eml.rindex('.'): #This will compare occurance of @ and . 
    print("Invalid Email ID plese enter valid ID...")

elif (eml.__len__())<eml.rindex('.'):   #This will compare email length with last index of . (dot)
    print("Invalid Email ID plese enter valid ID...")

elif (eml.__len__()-1)==eml.rindex('.'):  #This will nake shure email id not ending with . (dot)  
    print("Invalid Email ID plese enter valid ID...")







