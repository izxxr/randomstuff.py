import string
import random

def generate_unique_id(level=30):
	"""
	Generates a complex and safe to use unique ID. This is very useful when you need a
	key for AI response endpoint.
	
	Parameters:
		level (int) (optional):
			This determines how many chars will there be in the generated key. It is 30 by default.

	Returns:
		str: The generated string

	"""
	return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(level))
