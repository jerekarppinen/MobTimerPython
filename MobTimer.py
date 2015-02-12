#Developed in Python 2.7.6 environment
#Requires python-tk package installed
from timeit import default_timer as timer
from Tkinter import *
import Tkinter as tk
import os
import time

from collections import OrderedDict

import InputStringParser
import db

class MobTimer():

	def __init__(self):

		self.delta = 0

		self.displayTimer()			

	def displayTimer(self):

		self.root = tk.Tk()
		self.root.attributes("-zoomed", 1)

		self.usersText = tk.Text(width = 10, height = 0.8, font=('Helvetica', 28))
		self.usersText.pack()
		self.usersText.place(bordermode=OUTSIDE, height=50, width=300)

		self.addUserButton = Button(self.root, text="Add user", font='Helvetica', bg='lightblue', width=50, command=self.addUser)
		self.addUserButton.pack()
		self.addUserButton.place(bordermode=OUTSIDE, height=50, width=100, x=300)

		# retrieve added users from db
		users = db.getUsers()

		listbox = Listbox(self.root)
		listbox.pack()
		for row in users:
			listbox.insert(END, row[1])

		#deleteButton = Button(self.root, text="Delete", command=lambda listbox=listbox: listbox.delete(ANCHOR))
		deleteButton = Button(self.root, text="Delete", command=self.deleteFromList)
		deleteButton.pack()


		self.text = tk.Text(width = 10, height = 0.8, font=('Helvetica', 32))
		self.text.pack(side="top", expand=True)

		# if program was keyboard interrupted and there's some time left
		if self.delta > 0:
			self.text.insert(1.0, self.delta)
		elif self.delta == 0:
			self.text.insert(1.0, "15m")

		self.button = Button(self.root, text="Start the timer!", font='Helvetica', bg='lightblue', width=50, command=self.startTimer)
		self.button.pack(side="top", expand=True)

		self.root.mainloop()

	def deleteFromList(self):
		listbox.delete(ANCHOR)

	def startTimer(self):

		# todo: warn user if input is empty
		# and dont accept any other string-characters except for h,m,s
		inputRaw = str(self.text.get("1.0",END))

		# length == 1 equals empty input (for some reason)
		if len(inputRaw) == 1:
			self.root.destroy()
			self.displayTimer()

		try:
			inputRaw = int(inputRaw)
			inputParsed = inputRaw * 60
		except Exception as e:
			inputParsed = InputStringParser.InputStringParser(inputRaw).countTotalSeconds()

		self.root.withdraw()

		start = timer()
		while timer() - start <= inputParsed:

			# try - exception structure to detect if loop is terminated by key interrupt (ctrl+c)

			try:

				m, s = divmod(round(timer() - start, 2), 60)
				h, m = divmod(m, 60)
			 	sys.stdout.write("\rTime: %d:%02d:%02d" % (h, m, s))
				sys.stdout.flush()

				# sleep to lower CPU usage
				time.sleep(0.1)

				if timer() - start >= inputParsed:
					self.root.deiconify()
					break

			except KeyboardInterrupt:
				self.delta = self.seconds_to_human(inputParsed - (timer() - start))
				print "\nInterrupted"
				self.root.destroy()
				self.displayTimer()
				break

	# function taken from http://thomassileo.com/blog/2013/03/31/how-to-convert-seconds-to-human-readable-interval-back-and-forth-with-python/
	def seconds_to_human(self, seconds):

		interval_dict = OrderedDict([("Y", 365*86400), ("M", 30*86400), ("W", 7*86400), ("D", 86400), ("h", 3600), ("m", 60), ("s", 1)])      

		seconds = int(seconds)
		string = ""
		for unit, value in interval_dict.items():
			subres = seconds / value
			if subres:
				seconds -= value * subres
				string += str(subres) + unit
		return string

	def addUser(self):
		
		inputRaw = str(self.usersText.get("1.0",END))
		
		# if input is empty, destroy
		if len(inputRaw) == 1:
			self.root.destroy()
			self.displayTimer()

		db.addUser(inputRaw)

		self.root.destroy()
		self.displayTimer()




MobTimer()