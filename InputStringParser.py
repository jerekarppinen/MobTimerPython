class InputStringParser():
	def __init__(self, inputString):

		hPosition = inputString.find("h")
		mPosition = inputString.find("m")
		sPosition = inputString.find("s")

		# check if given string contains the positions
		# and find the time numbers if so
		# otherwise set to 0
		if hPosition > -1:
			self.hTimeNumber = self.getTimeNumber(hPosition, inputString)
		else:
			self.hTimeNumber = 0


		if mPosition > -1:
			self.mTimeNumber = self.getTimeNumber(mPosition, inputString)
		else:
			self.mTimeNumber = 0


		if sPosition > -1:
			self.sTimeNumber = self.getTimeNumber(sPosition, inputString)
		else:
			self.sTimeNumber = 0

	def getTimeNumber(self, find, inputString):

		number = ""

		for counter in range(find, 0, -1):
			if inputString[counter-1].isdigit():
				number += inputString[counter-1]
			else:
				break

		# reverse the found figure and return it
		return int(number[::-1])

	def countTotalSeconds(self):

		h = int(self.hTimeNumber)
		m = int(self.mTimeNumber)
		s = int(self.sTimeNumber)

		minutes = m * 60
		hours = h * 3600

		return minutes + s + hours