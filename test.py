name=input("Please enter name: ")
age=int(input("What's your age {0} ?\n".format(name)))

if (18 <= age < 31 ):
    print("Welcome {0} to 18-30 holiday".format(name))
else:
    print("Sorry,you can't enter") 
