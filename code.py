#!/usr/bin/python3

class CodeGenerator:

	def __init__(self):

		self.player = 'grant'
		self.difficulty = 1 # 0 is easy, 2 is difficult
		self.level = 2

	def __decode(self, letter):
		tt = ord(letter)
		if tt>=48 and tt<=57:
			return (tt - 48)
		if tt>=65 and tt<=86:
			return (tt - 55)
		return -1

	def __encode(self, number):
		if number < 10:
			return chr(number + 48)
		return chr(number + 55)

	def checksum(self, code):

		if len(code) != 7:
			return ''
		total = 0
		for i in range(0, 7):
			total = total + self.__decode(code[i])

		while total > 32:
			total = total - 32
		return self.__encode(total)


cg = CodeGenerator()

print(cg.checksum("2000001"))
print(cg.checksum("6VVVVVT"))
print(cg.checksum("2ETHJ01"))
print(cg.checksum("K21G002"))
print(cg.checksum("00VVVVT"))
