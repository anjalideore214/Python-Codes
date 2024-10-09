P=int(input("Enter the principal value:"))
R=float(input("Enter the rate of interest:"))
N=float(input("Enter the number of years:"))
SimpleInterest=(P*R*N)/100
CompoundInterest=P*(1+R/100)**N
print("Simple Interest on RS",P,"is RS",SimpleInterest,"For",N,"years")
print("Compound Interest on RS",P,"is RS",CompoundInterest,"For",N,"years")
