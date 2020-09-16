from tkinter import *
class Mall:
    def __init__(self,root):
        self.root = root
        self.root.title("Mall Management System")
        self.root.geometry("1350x700+0+0")
        title=Label(self.root,text="Mall Management System",bg="#1B9CFC",fg="#f5f6fa",font=("Bahnschrift Light SemiCondensed",40,"bold"))
        title.pack(side=TOP,fill=X)
        





root = Tk()
ob=Mall(root)

e=Entry(root,width=50)
e.pack()
e.get()
e.insert(0,"Enter your data")
buttonSubmit = Button(root,text="submit")
buttonSubmit.pack()
root.mainloop()
