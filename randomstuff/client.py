from .errors import *
from .constants import *
from .constants import _warn
from .joke import *
import aiohttp
import requests
import random

class Client:
	"""Represent a client
	
	Parameters
	----------
	key (str): Your API authentication key.
	version (str) (optional): The version number of API. It is 4 by default. Set it to 3 if you want to use v3.
	suppress_warnings (bool) (optional): If this is set to True, You won't get any console warnings. This does not suppress errors.

	Methods 
	-------

	get_ai_response(message: str, plan: str = '', **kwargs): Get random AI response.
	get_image(type: str = 'any'): Get random image.
	get_joke(type: str = 'any'): Get random joke.
	close(): Closes the session.

	"""
	def __init__(self, key: str, version: str = '4', suppress_warnings: bool = False):
		if version == '2':
			raise DeprecationWarning("Version 2 has been deprecated. Please migrate to version 4 as soon as possible.")
			return

		if not version in VERSIONS:
			raise VersionError("Invalid API version was provided. Use `3` or `4` only.")
			return

		self.version = "v"+version
		self.key = key
		self.suppress_warnings = suppress_warnings
		self.session = requests.Session()
		self.session.headers.update({'x-api-key': self.key})
		
		if self.version == 'v3':
			_warn(self, 'You are using v3 of API. Version 4 is out with improvements. Please migrate as soon as possible.\n')
		
	def get_ai_response(self, 
		message:str, 
		plan:str='', 
		**kwargs):
		"""Gets AI response

		This method has version based parameters
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		Common parameters:
			message (str) : The message to which response is required.
			plan (optional) (str) : The plan to use. This is optional and can only be used if API key has a paid plan registered.

			Above two parameters are not version specific they are supported in both versions.

		Version 3 specific:
			lang (optional) (str) : Language in which response is required. Defaults to `en`.
			type (optional) (str) : Language in which response is required. Defaults to `en`.
			bot_name (optional) (str) : The bot's name. Used in responses. Defaults to `RSA`
			dev_name (optional) (str) : The developer's name. Used in responses. Defaults to `PGamerX`
			unique_id (optional) (str) : The session specific user ID. Use this to make sessions for
									     certain user.
		
		Version 4 specific:
			language (optional) (str) : Language in which response is required. Defaults to `en`.
			server (optional) (str) : The server from which the response will be sent. Defaults to primary.
									  Set this to `backup` if the primary one isn't working. `unstable` is also
									  an option but don't use it as it is highly unstable.
			master (optional) (str) : The developer's name. Used in responses. Defaults to `PGamerX`
			bot (optional) (str) : The bot's name. Used in responses. Defaults to `RSA`
			uid (optional) (str) : The session specific user ID. Use this to make sessions for
							       certain user.
		
		Returns:
			str: The response as a string

		Raises:
			randomstuff.AuthError: The API key is invalid
			randomstuff.PlanError: Plan is either forbidden, invalid etc.
			randomstuff.ServerError: Specific to v4, Raised upon invalid server type.
		"""
		if not plan in PLANS:
			raise PlanError(F"Invalid Plan. Choose from {PLANS}")
			return

		if not kwargs.get('server', 'primary') in SERVERS:
			raise ServerError(f"Invalid server type choose from {SERVERS}.") 
			return

		if self.version == 'v3':
			params = {
				'message': message, 
				'lang': kwargs.get('lang', 'en'), 
				'type': kwargs.get('type', 'stable'), 
				'bot_name': kwargs.get('bot_name', 'RSA'), 
				'dev_name': kwargs.get('dev_name', 'PGamerX'),
				'unique_id': kwargs.get('unique_id', ''),
			}
			if plan == '':
				response = self.session.get(f'{BASE_URL}/v3/ai/response', params=params)
			else:
				response = self.session.get(f'{BASE_URL}/v3/{plan}/ai/response', params=params)

			if response.status_code == 401:
				raise AuthError(response.text)
				return


		elif self.version == 'v4':
			params = {
				'message': message, 
				'server': kwargs.get('server', 'primary'), 
				'master': kwargs.get('master', 'PGamerX'), 
				'bot': kwargs.get('bot', 'RSA'), 
				'uid': kwargs.get('uid', ''), 
				'language': kwargs.get('language', 'en'), 
			}

			if plan == '':
				response = self.session.get(f'{BASE_URL}/v4/ai', params=params)
			else:
				response = self.session.get(f'{BASE_URL}/v4/{plan}/ai', params=params)

			if response.status_code == 401:
				raise AuthError(response.text)
				return

			elif response.status_code == 403:
				raise PlanError(response.text)
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

		if self.version == 'v3':
			response = self.session.get(f'{BASE_URL}/v3/image/{type}')

		elif self.version == 'v4':
			response = self.session.get(f'{BASE_URL}/v4/image', params={'type': type})

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

		if self.version == 'v4':
			response = self.session.get(f'{BASE_URL}/{self.version}/joke', params={'type': type})
		elif self.version == 'v3':
			response = self.session.get(f'{BASE_URL}/{self.version}/joke/{type}')

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
	suppress_warnings (bool) (optional): If this is set to True, You won't get any console warnings. This does not suppress errors.


	Methods 
	-------

	async get_ai_response(message: str, plan: str = '', **kwargs): Get random AI response.
	async get_image(type: str = 'any'): Get random image.
	async get_joke(type: str = 'any'): Get random joke.
	async close(): Closes the session.
	
	"""
	def __init__(self, key: str, version: str = '3', suppress_warnings: bool = False):
		if version == '2':
			raise DeprecationWarning("Version 2 has been deprecated. Please migrate to version 4 as soon as possible.")
			return

		if not version in VERSIONS:
			raise VersionError("Invalid API version was provided. Use `3` or `4` only.")
			return

		self.version = "v"+version
		self.key = key
		self.suppress_warnings = suppress_warnings
		self.session = aiohttp.ClientSession(headers={'x-api-key': self.key})
		
		if self.version == 'v3':
			_warn(self, 'You are using v3 of API. Version 4 is out with improvements. Please migrate as soon as possible.\n')
		

	async def get_ai_response(self, 
		message:str, 
		plan:str='', 
		**kwargs):
		"""
		This function is a coroutine
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		Equivalent to `Client.get_ai_response`
		"""
		if not plan in PLANS:
			raise PlanError(F"Invalid Plan. Choose from {PLANS}")
			return

		if not kwargs.get('server', 'primary') in SERVERS:
			raise ServerError(f"Invalid server type choose from {SERVERS}.") 
			return

		if self.version == 'v3':
			params = {
				'message': message, 
				'lang': kwargs.get('lang', 'en'), 
				'type': kwargs.get('type', 'stable'), 
				'bot_name': kwargs.get('bot_name', 'RSA'), 
				'dev_name': kwargs.get('dev_name', 'PGamerX'),
				'unique_id': kwargs.get('unique_id', ''),
			}
			if plan == '':
				response = await self.session.get(f'{BASE_URL}/v3/ai/response', params=params)
			else:
				response = await self.session.get(f'{BASE_URL}/v3/{plan}/ai/response', params=params)

			if response.status == 401:
				raise AuthError(response.text)
				return

		elif self.version == 'v4':
			params = {
				'message': message, 
				'server': kwargs.get('server', 'primary'), 
				'master': kwargs.get('master', 'PGamerX'), 
				'bot': kwargs.get('bot', 'RSA'), 
				'uid': kwargs.get('uid', ''), 
				'language': kwargs.get('language', 'en'), 
			}

			if plan == '':
				response = await self.session.get(f'{BASE_URL}/v4/ai', params=params)
			else:
				response = await self.session.get(f'{BASE_URL}/v4/{plan}/ai', params=params)

			if response.status == 401:
				raise AuthError(response.text)
				return

			elif response.status == 403:
				raise PlanError(response.text)
				return

		return (await response.json())[0]['message']

	

	async def get_joke(self, type: str = 'any'):
		"""
		This function is a coroutine
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		Equivalent to `Client.get_joke`
		"""
		if self.version == 'v4':
			response = await self.session.get(f'{BASE_URL}/{self.version}/joke', params={'type': type})
		elif self.version == 'v3':
			response = await self.session.get(f'{BASE_URL}/{self.version}/joke/{type}')

		if response.status == 401:
			raise AuthError(response.text)

		return Joke(await response.json())

	async def get_image(self):
		"""
		This function is a coroutine
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		Equivalent to `Client.get_image`
		"""
		if not type in IMAGE_TYPES:
			raise TypeError(f"Image type not supported. Choose from {IMAGE_TYPES}")
			return

		if type == 'any':
			type = random.choice(IMAGE_TYPES)

		if self.version == 'v3':
			response = await self.session.get(f'{BASE_URL}/v3/image/{type}')

		elif self.version == 'v4':
			response =  await self.session.get(f'{BASE_URL}/v4/image', params={'type': type})
			

		return (await response.json())[0]

	async def close(self):
		"""
		This function is a coroutine
		----------------------------

		Closes a session

		"""
		await self.session.close()
