class Fish:
	def __init__(self):
		''' Constructor for this class. '''
		#Create some member animals
		self.members = ['Tuna', 'Nugget', 'Fillet']

	def printMembers(self):
		print("Printing members of the Fish class")
		for member in self.members:
			print('\t%s' % member)