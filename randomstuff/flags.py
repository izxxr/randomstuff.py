class Flags:
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
	def __init__(self, flags):
		self.nsfw = flags['nsfw']
		self.religious = flags['religious']
		self.political = flags['political']
		self.racist = flags['racist']
		self.sexist = flags['sexist']
		self.explicit = flags['explicit']