

from tkinter import *
def imprima_mes():
     print(radioValue)
     
app = Tk() 
app.geometry('300x300')

radioValue = IntVar() 

 
rdioOne = Radiobutton(app, text='Enero',
                             variable=radioValue, value=1) 
rdioTwo = Radiobutton(app, text='Febrero',
                             variable=radioValue, value=2) 
rdioThree = Radiobutton(app, text='Marzo',
                             variable=radioValue, value=3)
labelValue = Label(app, textvariable=radioValue).place(x=44,y=70)


rdioOne.grid(column=0, row=0)
rdioTwo.grid(column=0, row=1)
rdioThree.grid(column=0, row=2)

app.mainloop()
