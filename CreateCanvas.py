from tkinter import *
root=Tk()
root.title("This is canvas demo")
lbl=Label(root,text="Canvas")
cv=Canvas(root,bg="yellow",height=300,width=300)
coord=10,10,300,300
arc1=cv.create_arc(coord,start=0,extent=150,fill="pink")
arc2=cv.create_arc(coord,start=150,extent=215,fill="blue")
lbl.pack()
cv.pack()
root.mainloop()


