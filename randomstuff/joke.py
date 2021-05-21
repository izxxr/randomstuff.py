from .flags import *

class Joke:
	"""Represents a Joke

	Attributes
	----------

	category (str): The category of joke.
	type (str): The type of joke.
	joke (str or dict): The main joke. This can be a `dict` or `str` depending on joke's type.
						If joke's type is single then this will be `str` otherwise it will be a `dict`

	flags (randomstuff.Flags): The flags of joke. This is a `randomstuff.Flags` object. 
	id (int): The joke's ID.
	safe (bool): Determines if the joke is marked safe or not.
	lang (str): The language of the joke

	"""
	def __init__(self, data):
		self.category = data['category']
		self.type = data['type']
		if self.type == 'single':
			self.joke = data['joke']
		
		elif self.type == 'twopart':
			self.joke = {'setup': data['setup'], 'delivery': data['delivery']}

		self.flags = Flags(data['flags'])
		self.id = data['id']
		self.safe = data['safe']
		self.lang = data['lang']