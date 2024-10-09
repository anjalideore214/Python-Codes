User=input("Enter the Name of user :")
Age=int(input("Enter the Age of Voter :"))
if Age >= 18:
    print(User, "is of",Age ,"years old.So They Can give Vote")
else:
    print(User, "is of" ,Age, "years old.So They Cannot give Vote ")