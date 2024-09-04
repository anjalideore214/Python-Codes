import re
m=int(input("Enter mobile number"))
mob=str(m)
pattern='[7-9]{1}[0-9]{9}'
result=re.match(pattern,mob)
if result!=None:
    print("valid mobile number")
else:
    print("Invalid mobile number")

