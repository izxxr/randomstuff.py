from .errors import *
from .constants import *
from .joke import *
import aiohttp
import requests
import random

class Client:
	"""Represent a client
	
	Parameters
	----------
	key (str): Your API authentication key.

	"""
	def __init__(self, key: str):
		self.key = key
		self.session = requests.Session()
		self.session.headers.update({'x-api-key': self.key})

	def get_ai_response(self, message: str, lang: str = 'en', type: str = 'stable'):
		"""Gets AI response

		Parameters:
			message (str): The message to which response is required
			lang (str) (optional): The language in which response is required. By default this is english.
			type (str) (optional): The type of response. This is by default 'stable' and is recommended
								   to be stable.

		Returns:
			str: The response.

		Raises:
			randomstuff.AuthError: The API key was invalid.
		"""
		params = {'message': message, 'lang': lang, 'type': type}
		response = self.session.get(f'{BASE_URL}/v3/ai/response', params=params)

		if response.status_code == 401:
			raise AuthError(f"{message}: {solution}")
			return
		
		return response.json()[0]['message']

	def get_image(self, type: str = 'any'):
		"""Gets an image

		Parameters:
			type (str) (optional): The type of image. By default, it is 'any'.

		Returns:
			str: Link of image

		Raises:
			randomstuff.AuthError: The API key was invalid.
		"""
		if type == 'any':
			type = random.choice(IMAGE_TYPES)

		response = self.session.get(f'{BASE_URL}/v3/image/{type}')

		if response.status_code == 401:
			raise AuthError(f"{message}: {solution}")
			return

		return response.json()[0]

	def get_joke(self, type: str = 'any'):
		"""Gets a joke

		Parameters:
			type (str) (optional): The type of joke. By default, it is 'any'.

		Returns:
			randomstuff.Joke: The `randomstuff.Joke` object for the joke.

		Raises:
			randomstuff.AuthError: The API key was invalid.
		"""
		response = self.session.get(f'{BASE_URL}/v3/joke/{type}')
		if response.status_code == 401:
			raise AuthError(f"{message}: {solution}")
			return

		return Joke(response.json())

	def close(self):
		"""Closes the session"""
		self.session.close()

class AsyncClient:
	def __init__(self, key: str):
		self.key = key
		self.session = aiohttp.ClientSession(headers={'x-api-key': self.key})
	
	async def get_ai_response(self, message: str, lang: str = 'en', type: str = 'stable'):
		"""
		This function is a coroutine
		----------------------------

		Gets AI response.
	
		Parameters:
			message (str): The message to which response is required
			lang (str) (optional): The language in which response is required. By default this is english.
			type (str) (optional): The type of response. This is by default 'stable' and is recommended
								   to be stable.

		Returns:
			str: The response.

		Raises:
			randomstuff.AuthError: The API key was invalid.
		"""
		params = {'message': message, 'lang': lang, 'type': type}
		response = await self.session.get(f'{BASE_URL}/v3/ai/response', params=params)

		if response.status == 401:
			raise AuthError(f"{message}: {solution}")
			return
		
		return (await response.json())[0]['message']

	async def get_image(self, type: str = 'any'):
		"""Gets an image

		Parameters:
			type (str) (optional): The type of image. By default, it is 'any'.

		Returns:
			str: Link of image

		Raises:
			randomstuff.AuthError: The API key was invalid.
		"""
		if type == 'any':
			type = random.choice(IMAGE_TYPES)

		response = await self.session.get(f'{BASE_URL}/v3/image/{type}')

		if response.status == 401:
			raise AuthError(f"{message}: {solution}")
			return

		return (await response.json())[0]

	async def get_joke(self, type: str = 'any'):
		"""Gets a joke

		Parameters:
			type (str) (optional): The type of joke. By default, it is 'any'.

		Returns:
			randomstuff.Joke: The `randomstuff.Joke` object for the joke.

		Raises:
			randomstuff.AuthError: The API key was invalid.
		"""
		response = await self.session.get(f'{BASE_URL}/v3/joke/{type}')
		if response.status == 401:
			raise AuthError(f"{message}: {solution}")
			return

		return Joke(await response.json())

	async def close(self):
		"""Closes a session"""
		await self.session.close()