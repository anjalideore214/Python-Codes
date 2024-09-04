class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if(self.a<other.a):
            return "obj1 is less than obj2"
        else:
            return "obj2 is less than obj1"


    def __gt__(self,other):
        if(self.a>other.a):
            return "obj1 is greater than obj2"
        else:
            return "obj2 is greater than obj1"


    def __eq__(self,other):
        if(self.a==other.a):
            return "obj1 is equal to bj2"
        else:
            return "obj2 is not equal to obj1"

obj1=A(21)
obj2=A(13)
print(obj1<obj2)
obj1=A(2)
obj2=A(3)
print(obj1>obj2)
obj3=A(6)
obj4=A(6)
print(obj3==obj4)
 


    


    
        
