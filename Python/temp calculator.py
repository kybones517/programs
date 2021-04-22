from tkinter import *

width = "220"
height = "250"
root = Tk()
root.title("Caluculator") 
root.geometry(width+"x"+height)

root.columnconfigure(0, weight=1)

displayFrame = Frame(root)

displayFrame.grid(row=0,column = 0,sticky='ew')
displayFrame.columnconfigure(0,weight =1)
btnFrame = Frame(root)
btnFrame.grid(row=1,column=0,sticky ="ew",padx=5,pady=2)


textBox = Label(displayFrame, text="Text Box",relief = "ridge",background ="#CCFFFF")
textBox.grid(row=0,column = 0,sticky='ew', padx = 10, pady=10,ipadx=10,ipady=10) 


def updateTextBox(x):
    print("Button workds")
    global textBox
    textBox.configure(text=x)
    

testBtn = Button(btnFrame,text="1", command=lambda: textBox.configure(text=1))
testBtn2 = Button(btnFrame,text="2",command=lambda: textBox.configure(text=2))
testBtn3 = Button(btnFrame,text="3",command=lambda: textBox.configure(text=3))
testBtn4 = Button(btnFrame,text="4",command=lambda: textBox.configure(text=4))
testBtn.grid(row=1,column =0,padx=15,ipadx=7)
testBtn2.grid(row=1,column =1,padx=10,ipadx=7)
testBtn3.grid(row=1,column =2,padx=10,ipadx=7)
testBtn4.grid(row=1,column =3,padx=10,ipadx=7)

root.mainloop()
