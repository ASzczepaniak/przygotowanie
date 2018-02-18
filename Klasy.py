import math


class Macierz:
	def __init__(self, tablica):
		if math.sqrt(len(tablica)).is_integer():
			self.tablica = tablica
			self.rozmiar = int(math.sqrt(len(tablica)))
		else:
			self.tablica = [1,0,1,0]
			self.rozmiar = 2


	def getTablica(self):
		return self.tablica
	def setTablica(self, tablica):
		self.tablica = tablica

	def getRozmiar(self):
		return self.rozmiar
	def setRozmiar(self, rozmiar):
		self.rozmiar = rozmiar

	def __len__(self):
		return self.rozmiar

	def __str__(self):
		macierzString = "["
		for i in range(len(self)):
			for j in range(len(self)):
				macierzString = macierzString + str(self.tablica[i*2 + j]) + ", "
			macierzString = macierzString + "\n"
		macierzString = macierzString[:len(macierzString)-3] + "]"
		return macierzString

	def __add__(self, otherMarcierz):
		if len(self.tablica) == len(otherMarcierz.tablica):
			macierz = Macierz([])
			for i in range(len(self.tablica)):
				macierz.tablica.append(self.tablica[i] + otherMarcierz.tablica[i])
			macierz.rozmiar = self.rozmiar
			return macierz
		else:
			print "ZLE WYMIARY"

	def __sub__(self, otherMarcierz):
		if len(self.tablica) == len(otherMarcierz.tablica):
			macierz = Macierz([])
			for i in range(len(self.tablica)):
				macierz.tablica.append(self.tablica[i] - otherMarcierz.tablica[i])
			macierz.rozmiar = self.rozmiar
			return macierz
		else:
			print "ZLE WYMIARY"

#	def translacja(self):
#		tablica = []
#		for i in range(len(self.tablica)):
#			print((i%3)*self.rozmiar+int(i/self.rozmiar))
#			tablica.append(self.tablica[(i%3)*self.rozmiar+int(i/self.rozmiar)])
#			print tablica
#		self.tablica = tablica



#macierz1 = Macierz([2,3,4,5,4,3,7,8,6])
#macierz2 = Macierz([3,4,5,6])

#macierz3 = macierz2 + macierz1
#macierz4 = macierz1 - macierz2

#macierz1.translacja()





