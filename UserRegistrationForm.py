from tkinter import *
root=Tk()
root.title("User Registration Form ")
l1=Label(root,text="Enter UserName:")
e1=Entry(root,text='Username')
l2=Label(root,text="Enter Password:")
e2=Entry(root,text='password')
l1.place(x=100,y=30)
e1.place(x=200,y=70)
l2.place(x=100,y=70)
e2.place(x=200,y=30)
Button(root,text="Submit",background="yellow",foreground="red",command=lambda:print("Responce Submitted...🤗")).place(x=90,y=120)
Button(root,text="Reset",background="yellow",foreground="red",command=root.destroy).place(x=150,y=120)
root.mainloop()