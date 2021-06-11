class BaseObject:
	"""Super class for most of the objects used in the library

	Attributes
	----------
	data (dict) : The raw data as returned by API.
	is_response : 

	"""
	def __init__(self, data, **kwargs):
		self.data = data
		self.is_ai_response = kwargs.get('is_ai_response', False)
		self.is_joke = kwargs.get('is_joke', False)

		if self.is_ai_response:
			self.message = data[0].get('message')
			self.success = data[0].get('success', None) # NoneType when using version 4
			self.api_key = data[0].get('api_key', None) # NoneType when using version 4
			
			if self.success == None:
				self.response_time = data[1].get('response_time') # NoneType in version 3
			else:
				self.response_time = None
			return

		if self.is_joke:
			if self.data['type'] == 'twopart':
				setattr(self, 'joke', {'setup': self.data['setup'], 'delivery': self.data['delivery']})
			else:
				setattr(self, 'joke', self.data['joke'])

		for _ in self.data.keys():
			if _ == 'flags':
				setattr(self, _, Flags(self.data[_]))
			elif _ in ['setup', 'twopart']:
				pass
			else:
				setattr(self, _, self.data[_])


class Joke(BaseObject):
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
		super().__init__(data, is_joke=True)

class AIResponse(BaseObject):
	"""Represents an AI response returned from `get_ai_response` method.
	
	Attribues
	---------

	message : The main message.
	response_time : The response time returned by API.
	"""
	def __init__(self, data):
		super().__init__(data, is_ai_response=True)

class Flags(BaseObject):
	"""Represents a joke's flags

	Attributes
	----------

	nsfw (bool): Determines if the joke is marked NSFW or not.
	religious (bool): Determines if the joke is marked religious or not.
	political (bool): Determines if the joke is marked political or not.
	racist (bool): Determines if the joke is marked racist or not.
	sexist (bool): Determines if the joke is marked sexist or not.
	explicit (bool): Determines if the joke is marked explicit or not.
	"""
	def __init__(self, data):
		super().__init__(data)

class Waifu(BaseObject):
	"""Represents a waifu returned by API

	Attributes
	----------
	
	url (str) : The URL to waifu image.
	"""
	def __init__(self, data):
		super().__init__(data)
