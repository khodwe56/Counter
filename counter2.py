import  tkinter as tk
import tkinter.font as tkFont

window = tk.Tk()
window.title("Counter")
window.configure(bg = "dark blue",width = 500,height = 500)
window.geometry("500x500")

window.counter = 0


fontStyle = tkFont.Font(family="gothic", size=20)
buttonFont = tkFont.Font(size = 15)

def increment():
	window.counter += 1
	textLabel['text'] = str(window.counter)


def decrement():
	window.counter -= 1
	textLabel['text'] = str(window.counter)


def reset():
	window.counter = 0
	textLabel['text'] = str(window.counter)



textLabel = tk.Label(window,text = str(window.counter),width = 5,height = 5,font = fontStyle)
textLabel.configure(fg = 'dark green',bg = 'black')
textLabel.pack(anchor = 'center',pady = 10,side = 'top',fill = 'both')

incB = tk.Button(window,text = "+",command = increment,width = 10,font = buttonFont)
decB = tk.Button(window,text = "-",command = decrement,width = 10,font = buttonFont)
resetB = tk.Button(window,text = "Reset",command = reset,font = buttonFont)

incB.configure(bg = 'silver')
decB.configure(bg = 'silver')
resetB.configure(bg = 'silver')
incB.place(x = 60,y = 250)
#incB.pack(anchor = 'center',pady = 10)
decB.place(x = 310,y = 250)
#decB.pack(anchor = 'center',pady = 10)
resetB.place(x = 210,y = 370)
#resetB.pack(anchor = 'center',pady = 10,side = 'bottom')


window.mainloop()	

