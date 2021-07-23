#!/usr/bin/python3

from random import randint

class JurassicParkPasswordGenerator:

	def __init__(self):

		self.__player = 'grant'
		self.__difficulty = 2 # 1 is easy, 3 is difficult
		self.__level = 1 # 1-7 for grant, 1-5 for raptor
		self.__weapons = [60, 60, 60, 60, 60, 60, 60]

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

	def __checksum(self, code):

		if len(code) != 7:
			return ''
		total = 0
		for i in range(0, 7):
			total = total + self.__decode(code[i])

		while total >= 32:
			total = total - 32
		return self.__encode(total)

	def __to_bits(self, number):

		return [True if digit=='1' else False for digit in bin(number)[2:]]

	def __to_int(self, bits):

		x = 1
		ret = 0
		buffer = bits
		while len(buffer) > 0:
			if buffer.pop():
				ret = ret + x
			x = x * 2
		return ret

	def __random(self, length=1):

		ret = ''
		for i in range(0, length):
			ri = randint(0, 31)
			if ri < 10:
				ret = ret + chr(ri + 48)
			else:
				ret = ret + chr(ri + 55)
		return ret

	def __get_password(self):

		if self.__player == 'raptor':

			levels = ['G', 'I', 'K', 'M', 'O']
			ret = levels[(self.__level - 1)]
			ret = ret + self.__random(5)
			ret = ret + str(self.__difficulty)
			ret = ret + self.__checksum(ret)

			return ret

		if self.__player == 'grant':

			levels = ['0', '2', '4', '6', '8', 'A', 'C']
			data = []
			for ammo in self.__weapons:
				mod_ammo = int(ammo / 4)
				if mod_ammo > 15:
					mod_ammo = 15
				chunk = ([False, False, False, False, False] + self.__to_bits(mod_ammo))[-4:]
				data = data + chunk
			chunk = ([False, False] + self.__to_bits(self.__difficulty))[-2:]
			data = data + chunk

			ret = levels[(self.__level - 1)]
			while len(data) >= 5:
				ret = ret + self.__encode(self.__to_int(data[0:5]))
				data = data[5:]
			ret = ret + self.__checksum(ret)
			return ret

	def __set_password(self, password):

		raise NotImplementedError

	def level(self, level_number=None):

		if not(isinstance(level_number, (int))):
			return self.__level
		if level_number < 1:
			return self.__level
		if level_number > 7:
			return self.__level
		if ((self.__player == 'raptor') & (level_number > 5)):
			return self.__level
		self.__level = level_number
		return level_number

	def difficulty(self, n=None):

		if not(isinstance(n, (int))):
			return self.__difficulty
		if n < 1:
			return self.__difficulty
		if n > 3:
			return self.__difficulty
		self.__difficulty = n
		return n

	def weapon(self, weapon_id, value=None):

		if not(isinstance(weapon_id, (int))):
			return None
		if weapon_id < 1:
			return None
		if weapon_id > 7:
			return None
		if not(isinstance(value, (int))):
			return self.__weapons[weapon_id - 1]
		if value < 0:
			return self.__weapons[weapon_id - 1]
		if value > 60:
			return self.__weapons[weapon_id - 1]
		self.__weapons[weapon_id - 1] = value
		return value

	def player(self, player=None):

		if player == 'grant':
			self.__player = 'grant'
		if player == 'raptor':
			self.__player = 'raptor'
			if self.__level > 5:
				self.__level = 5
		return self.__player

	def password(self, password=''):

		if len(password) == 8:
			return self.__set_password(password)
		else:
			return self.__get_password()


