Number=int(input("Enter number to create multiplication table:"))
for i in range(1,11,1):
    num1=Number*i
    print(Number,'*',i,'=',num1)
    i+=1
