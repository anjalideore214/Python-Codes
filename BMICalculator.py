height=float(input("Enter your height in cm:"))
weight=float(input("Enter your weight in Kg:"))
BMI= weight/(height/100)**2
print(f"Your BMI is {BMI}")
if BMI<=18.4:
    print("You are underweight.")
elif BMI<=24.9:
    print("You are Healthy.")
elif BMI<=29.9:
    print("You are Over Weight.")
elif BMI<=34.9:
    print("You are severely Over Weight.")
elif BMI<=39.9:
    print("You are Obese.")
else:
    print("You are severely Obese.")