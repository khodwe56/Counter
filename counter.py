import tkinter as tk

window = tk.Tk()
window.title("Counter")
window.geometry("500x500")
window.configure(bg = "black")

label = tk.Label(window,text = "Counter")
label.grid(row =0,column = 750)
# label.pack(anchor="center")
value = 0
#def incmentor:
textLabel = tk.Label(window,text = str(value))
textLabel.grid(row = 1,column = 750)
# textLabel.pack(anchor = "center")	

def addText(countVal):
	textLabel = tk.Label(window,text = str(countVal))
	textLabel.grid(row = 1,column = 750)


def increment():
	global value
	value += 1
	addText(value)
	# textLabel.grid(row = 1,column = 750)
	# textLabel.pack(anchor = "center")	

def decrement():
	global value
	value -= 1
	if value <= 0:
		value = 0
	addText(value)	
	# textLabel = tk.Label(window,text = str(value))
	# textLabel.grid(row = 1,column = 750)
	# textLabel.pack(anchor = "center")

def reset():
	global value
	value = 0
	addText(value)
	# textLabel = tk.Label(window,text = str(value))
	# textLabel.grid(row = 1,column = 750)
	# textLabel.pack(anchor = "center")		

incB = tk.Button(window,text = "+",command=increment)
decB = tk.Button(window,text = "-",command=decrement)
resetB = tk.Button(window,text = "Reset",command=reset)
resetB.grid(row = 2,column = 750)
incB.grid(row = 3,column = 750)
decB.grid(row = 4,column = 750)

# resetB.pack(anchor = "center")
# incB.pack(anchor = "center")
# decB.pack(anchor = "center")



window.mainloop()