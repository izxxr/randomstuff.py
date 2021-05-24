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
	version (str) (optional): The version number of API. It is 3 by default set it to 2 if you want to use v2.

	Methods 
	-------

	get_ai_response(message: str, lang: str = 'en', type: str = 'stable'): Get random AI response.
	get_image(type: str = 'any'): Get random image.
	get_joke(type: str = 'any'): Get random joke.

	"""
	def __init__(self, key: str, version: str = '3'):
		if not version in VERSIONS:
			raise VersionError("Invalid API version was provided. Use `2` or `3` only.")
			return

		self.version = "v"+version
		self.key = key
		self.session = requests.Session()
		self.session.headers.update({'x-api-key': self.key})

	def get_ai_response(self, message: str, lang: str = 'en', type: str = 'stable', plan: str = None):
		"""Gets AI response

		Parameters:
			message (str): The message to which response is required
			lang (str) (optional): The language in which response is required. By default this is english.
			type (str) (optional): The type of response. This is by default 'stable' and is recommended
								   to be stable.
			plan (str) (optional): If you have a plan for RandomAPI pass the plan's name in this argument. `randomstuff.constants.PLAN` for list of plans.

		Returns:
			str: The response.

		Raises:
			randomstuff.AuthError: The API key was invalid.
			randomstuff.PlanError: Invalid Plan
			randomstuff.VersionError: Unsupported or invalid version.
		"""
		if not plan in PLANS:
			raise PlanError(F"Invalid Plan. Choose from {PLANS}")
			return

		if self.version == 'v2' and plan != None:
			raise VersionError(f"v2 does not support {plan} plan.")
			return


		
		if self.version == 'v2':
			response = self.session.get(f'{BASE_URL}/ai/response?message={message}&language={lang}&api_key={self.key}')
			return response.json()[0]

		elif self.version == 'v3' and plan == None:
			params = {'message': message, 'lang': lang, 'type': type}
			response = self.session.get(f'{BASE_URL}/v3/ai/response', params=params)
			if response.status_code == 401:
				raise AuthError(response.text)
				return
			return response.json()[0]['message']
		
		elif self.version == 'v3' and plan != None:
			params = {'message': message, 'lang': lang, 'type': type}
			response = self.session.get(f'{BASE_URL}/v3/{plan}/ai/response', params=params)
			return response.text
			if response.status_code == 401:
				raise AuthError(response.text)
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

		if self.version == 'v2':
			response = self.session.get(f'{BASE_URL}/image/{type}?api_key={self.key}')

		elif self.version == 'v3':
			response = self.session.get(f'{BASE_URL}/v3/image/{type}')

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

		if self.version == 'v2':
			response = self.session.get(f'{BASE_URL}/joke/{type}?api_key={self.key}')

		elif self.version == 'v3':
			response = self.session.get(f'{BASE_URL}/v3/joke/{type}')

		if response.status_code == 401:
			raise AuthError(response.text)

		return Joke(response.json())

	def close(self):
		"""Closes the session"""
		self.session.close()

class AsyncClient:
	"""Represent an async client. This is same as `randomstuff.Client` but is suitable for async programs.
	
	Parameters
	----------
	key (str): Your API authentication key.
	version (str) (optional): The version number of API. It is 3 by default set it to 2 if you want to use v2.


	Methods 
	-------

	async get_ai_response(message: str, lang: str = 'en', type: str = 'stable'): Get random AI response.
	async get_image(type: str = 'any'): Get random image.
	async get_joke(type: str = 'any'): Get random joke.
	
	"""
	def __init__(self, key: str, version: str = '3'):
		if not version in VERSIONS:
			raise TypeError("Invalid API version was provided. Use `2` or `3` only.")
			return

		self.version = "v"+version
		self.key = key
		self.session = aiohttp.ClientSession(headers={'x-api-key': self.key})
	
	async def get_ai_response(self, message: str, lang: str = 'en', type: str = 'stable', plan: str = None):
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
		if not plan in PLANS:
			raise PlanError(f"Invalid Plan. Choose from {PLANS}")
			return

		if self.version == 'v2' and plan != None:
			raise VersionError(f"v2 does not support {plan} plan.")
			return

		
		if self.version == 'v2':
			response = await self.session.get(f'{BASE_URL}/ai/response?message={message}&language={lang}&api_key={self.key}')
			return (await response.json())[0]

		elif self.version == 'v3' and plan == None:
			params = {'message': message, 'lang': lang, 'type': type}
			response = await self.session.get(f'{BASE_URL}/v3/ai/response', params=params)
			
			if response.status == 401:
				raise AuthError(response.text)
				return
				
			return (await response.json())[0]['message']

		elif self.version == 'v3' and plan != None:
			params = {'message': message, 'lang': lang, 'type': type}
			response = await self.session.get(f'{BASE_URL}/v3/{plan}/ai/response', params=params)
			
			if response.status == 401:
				raise AuthError(response.text)
				return

			return (await response.json())[0]['message']



	async def get_image(self, type: str = 'any'):
		"""
		This function is a coroutine
		----------------------------

		Gets an image

		Parameters:
			type (str) (optional): The type of image. By default, it is 'any'.

		Returns:
			str: Link of image

		Raises:
			randomstuff.AuthError: The API key was invalid.
		"""
		if type == 'any':
			type = random.choice(IMAGE_TYPES)

		if self.version == 'v2':
			response = await self.session.get(f'{BASE_URL}/image/{type}?api_key={self.key}')

		elif self.version == 'v3':
			response = await self.session.get(f'{BASE_URL}/v3/image/{type}')

		if response.status == 401:
			raise AuthError(response.text)

		return (await response.json())[0]

	async def get_joke(self, type: str = 'any'):
		"""
		This function is a coroutine
		----------------------------

		Gets a joke

		Parameters:
			type (str) (optional): The type of joke. By default, it is 'any'.

		Returns:
			randomstuff.Joke: The `randomstuff.Joke` object for the joke.

		Raises:
			randomstuff.AuthError: The API key was invalid.
		"""
		if self.version == 'v2':
			response = await self.session.get(f'{BASE_URL}/joke/{type}?api_key={self.key}')

		elif self.version == 'v3':
			response = await self.session.get(f'{BASE_URL}/v3/joke/{type}')
		
		if response.text == 401:
			raise AuthError(response.text)

		return Joke(await response.json())

	async def close(self):
		"""
		This function is a coroutine
		----------------------------

		Closes a session

		"""
		await self.session.close()
