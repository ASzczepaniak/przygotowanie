class Auto:
	color = "red"
	name = ""
	price = 20000

	def Description(self):
		print "My car {} is {} for {}".format(self.name, self.color, self.price)

car1 = Auto()

car1.name = "Ziutek"

car1.Description()