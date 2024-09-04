class student:
    def __init__(self,n=' ',m=0):
        self.name=n
        self.marks=m
    def show(self):
        print("Hello ",self.name)
        print("Your Marks are:",self.marks)
    def calc(self):
        if(self.marks>600):
            print("You got First class ")
        elif(self.marks>500):
            print("You got Second class")
        elif(self.marks>300):
            print("You got Third class")
        else:
            print("You are FAILED")

n=int(input("Enter Number of Students:-"))
i=0
while(i<n):
    print("Enter the Name of Student:-")
    name=input()
    print("Enter Total Marks secured:-")
    marks=int(input())
    s=student(name,marks)
    s.show()
    s.calc()
    i+=1
    print("**********************************************")
