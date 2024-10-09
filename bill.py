from tkinter import * 
import random 
class Bill_App:
    def __init__(self, root): 
        self.root = root 
        self.root.geometry("1300x700+0+0") 
        self.root.maxsize(width=1280, height=700) 
        self.root.minsize(width=1280, height=700) 
        self.root.title("Billing Software") 
        # ====================Variables========================# 
        self.cus_name = StringVar() 
        self.c_phone = StringVar() 
        # For Generating Random Bill Numbers 
        x = random.randint(1000, 9999) 
        self.c_bill_no = StringVar() 
        # Seting Value to variable# 
        self.c_bill_no.set(str(x)) 
        self.bath_soap = IntVar() 
        self.face_cream = IntVar() 
        self.face_wash = IntVar() 
        self.hair_spray = IntVar() 
        self.body_lotion = IntVar() 
        self.rice = IntVar() 
        self.daal = IntVar() 
        self.food_oil = IntVar() 
        self.wheat = IntVar() 
        self.sugar = IntVar() 
        self.maza = IntVar() 
        # self.cok...
        root=Tk()
        object=Bill_App(root)
        root.mainloop()
