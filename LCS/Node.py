class Node:
	""" Represents a node for LCS matrix """
	def __init__(self, val, from_node = None, forChar = False):
		self.from_node = from_node
		self.val = val
		self.forChar = forChar

	def __add__(self, other):
		return self.val + other.val

	def __gt__(self, other):
		if(self.val>other.val):
			return True
		else:
			return False

	def __lt__(self, other):
		if(self.val<other.val):
			return True
		else:
			return False

	def __eq__(self, other):
		if(self.val==other.val):
			return True
		else:
			return False
	def getChar(self):
		""" Returns the Common Character for which this Node is or False """
		return self.forChar