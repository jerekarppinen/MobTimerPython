#Developed in Python 2.7.6 environment
#Requires python-tk package installed
from timeit import default_timer as timer
from Tkinter import *
import Tkinter as tk
import os
import time

def startTimer():
	
	input = int(text.get("1.0",END))
	root.withdraw()

	start = timer()
	while timer() - start <= input * 60:
		#print round(timer() - start,2)
		m, s = divmod(round(timer() - start,2), 60)
		h, m = divmod(m, 60)
		sys.stdout.write("\rTime: %d:%02d:%02d" % (h, m, s))
		#os.system("cls" if os.name == "nt" else "clear")
		if timer() - start >= input * 60:
			root.deiconify()
			break
		time.sleep(0.1)

root = tk.Tk()
root.attributes("-zoomed", 1)

text = tk.Text(width = 30, height = 0.8, font=('Helvetica', 32))
text.pack(side="top", expand=True)
text.insert(1.0, "15")

button = Button(root, text="Start the timer!", font='Helvetica', bg='lightblue', width=50, command=startTimer)
button.pack(side="top", expand=True)

root.mainloop()

