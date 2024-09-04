A=int(input("Enter the number 1:-"))
B=int(input("Enter the number 2:-"))
#Arithmatic operator
print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(A%B)
print(A//B)
print(A**B)
#Relational operator
C=int(input("Enter the number1:-"))
D=int(input("Enter the number2:-"))
print(C>D)
print(C<D)
print(C==D)
print(C>=D)
print(C<=D)
print(C!=D)
#Logical operator
M=bool(input("Enter the value1:-"))
N=bool(input("Enter the value2:-"))

if((M and N)==M):
    print("True")
else :
    print("False")

if((M or N)==N):
    print("True")
else :
    print("False")
#Bitwise operator    
print(C & D)
print(C | D)
print(~(C))
print(A ^ B)
print(A >> 2)
print(B << 5)
