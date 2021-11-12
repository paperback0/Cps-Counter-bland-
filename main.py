from tkinter import *
from threading import Timer

choose = input("How many seconds: ")
choose = int(choose)

turn = 0
cps = 0
num = 0

window = Tk()
window.geometry("800x600")



def cps2():
    global num
    cps = num/choose
    cps = str(cps)
    Your_cps = Entry(window)
    Your_cps.insert(END, "Your cps: " + cps)
    Your_cps.pack()

cpstrack = Timer(choose, cps2 )

def addcps():
    global num
    num += 1


def runcps():
    global turn
    if turn == 1:
        addcps()

    if turn == 0:
        cpstrack.start()
        turn =+ 1
        ClicktoStart['text'] = "Click"


ClicktoStart = Button(window, text="Click To Start", padx=200, pady=100, command=runcps)
ClicktoStart.pack()

window.mainloop()