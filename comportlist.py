import serial.tools.list_ports
from tkinter import *
ports = serial.tools.list_ports.comports()
a=[]
for port, desc, hwid in sorted(ports):
        a.append(desc)
print(a)


master = Tk()
master.geometry("500x100")
variable = StringVar(master)
variable.set(a[0]) # default value
w = OptionMenu(master, variable, *a)
w.place(x=120,y=10)
# w.pack()
def ok():
    print ("Selected Option is: " + variable.get())

button = Button(master, text="    OK     ", command=ok)
button.place(x=240, y=50)
# button.pack()

mainloop()