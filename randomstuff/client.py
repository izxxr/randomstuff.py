from .errors import *
from .constants import *
from .objects import *
from ._helper import _check_coro, _check_status, _warn
import aiohttp
import inspect
import requests
import random

class Client:
	"""Represent a client
	
	Parameters
	----------
	api_key (str): Your API authentication key.
	version (str) (optional): The version number of API. It is 4 by default. Set it to 3 if you want to use v3.
	suppress_warnings (bool) (optional): If this is set to True, You won't get any console warnings. This does not suppress errors.

	Methods 
	-------

	get_ai_response(message: str, plan: str = '', **kwargs): Get random AI response.
	get_image(type: str = 'any'): Get random image.
	get_joke(type: str = 'any'): Get random joke.
	close(): Closes the _session.

	"""
	def __init__(self, api_key: str, version: str = '4', suppress_warnings: bool = False):
		if version in DEPRECATED_VERSIONS:
			raise DeprecationWarning(f"Version {version} has been deprecated. Please migrate to version {version[-1]} as soon as possible.")
			return

		if not version in VERSIONS:
			raise InvalidVersion("Invalid API version was provided. Use `3` or `4` only.")
			return

		self.version = version
		self.api_key = api_key
		self.suppress_warnings = suppress_warnings
		self._base_url = BASE_URL + "/" + "v" + self.version
		self._session = requests.Session()
		self._session.headers.update({'x-api-key': self.api_key})
		
		if self.version == '3':
			_warn(self, 'You are using v3 of API. Version 4 is out with improvements. Please migrate as soon as possible.\n')
	

	def get_ai_response(self, 
		message:str, 
		plan:str='', 
		**kwargs) -> AIResponse:
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
			unique_id (optional) (str) : The _session specific user ID. Use this to make _sessions for
									     certain user.
		
		Version 4 specific:
			language (optional) (str) : Language in which response is required. Defaults to `en`.
			server (optional) (str) : The server from which the response will be sent. Defaults to primary.
									  Set this to `backup` if the primary one isn't working. `unstable` is also
									  an option but don't use it as it is highly unstable.
			master (optional) (str) : The developer's name. Used in responses. Defaults to `PGamerX`
			bot (optional) (str) : The bot's name. Used in responses. Defaults to `RSA`
			uid (optional) (str) : The _session specific user ID. Use this to make _sessions for
							       certain user.
		
		Returns:
			AIResponse: The response as an AI Response object.

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

		_check_coro(self)

		if self.version == '3':
			params = {
				'message': message, 
				'lang': kwargs.get('lang', 'en'), 
				'type': kwargs.get('type', 'stable'), 
				'bot_name': kwargs.get('bot_name', 'RSA'), 
				'dev_name': kwargs.get('dev_name', 'PGamerX'),
				'unique_id': kwargs.get('unique_id', ''),
			}
			if plan == '':
				response = self._session.get(f'{self._base_url}/ai/response', params=params)
			else:
				response = self._session.get(f'{self._base_url}/{plan}/ai/response', params=params)

		elif self.version == '4':
			params = {
				'message': message, 
				'server': kwargs.get('server', 'primary'), 
				'master': kwargs.get('master', 'PGamerX'), 
				'bot': kwargs.get('bot', 'RSA'), 
				'uid': kwargs.get('uid', ''), 
				'language': kwargs.get('language', 'en')
			}

			if plan == '':
				response = self._session.get(f'{self._base_url}/ai', params=params)
			else:
				response = self._session.get(f'{self._base_url}/{plan}/ai', params=params)

		_check_status(response)

		return AIResponse(response.json())

	
	def get_image(self, type: str = 'any') -> str:
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

		if not type in IMAGE_TYPES:
			raise InvalidType('Invalid image type provided.')
			return

		_check_coro(self)

		if self.version == '3':
			response = self._session.get(f'{self._base_url}/image/{type}')

		elif self.version == '4':
			response = self._session.get(f'{self._base_url}/image', params={'type': type})

		_check_status(response)

		return response.json()[0]

	def get_joke(self, type: str = 'any') -> Joke:
		"""Gets a joke

		Parameters:
			type (str) (optional): The type of joke. By default, it is 'any'.

		Returns:
			randomstuff.Joke: The `randomstuff.Joke` object for the joke.

		Raises:
			randomstuff.AuthError: The API key was invalid.
		"""
		

		if not type in JOKE_TYPES:
			raise InvalidType('Invalid Joke type provided.')
			return

		_check_coro(self)

		if self.version == '4':
			response = self._session.get(f'{self._base_url}/joke', params={'type': type})
		
		elif self.version == '3':
			response = self._session.get(f'{self._base_url}/joke/{type}')

		_check_status(response)

		return Joke(response.json())

	def get_waifu(self, plan:str, type:str):
		"""Gets a random waifu pic (SFW)
		
		Parameters:
			type (str) : The type of waifu. Can be one from the table below:
			
			|:-------:|
			|  Types  |
			|:-------:|
			|  waifu  |
			|  neko   |
			| shinobu |
			| megumin |
			|  bully  |
			| cuddle  |
			|:-------:|

		Returns:	
			Waifu

		Raises:
			BadAPIKey: The API key was invalid.
			HTTPError: An error occured while connecting to API.

		"""
		if self.version == '3':
			raise InvalidVersion("Version 3 does not support this method.")
			return

		if not type in WAIFU_TYPES:
			raise InvalidType("Invalid waifu type provided")
			return

		if not plan in PLANS:
			raise InvalidPlanError("The plan provided is invalid.")

		_check_coro(self)

		response = self._session.get(f"{self._base_url}/pro/waifu", params={'type': type})

		_check_status(response)

		return Waifu(response.json()[0])

	def close(self):
		"""Closes the _session"""
		self._session.close()

class AsyncClient(Client):
	"""Represent an async client. This is same as `randomstuff.Client` but is suitable for async programs.
	
	Parameters
	----------
	api_key (str): Your API authentication key.
	version (str) (optional): The version number of API. It is 3 by default set it to 2 if you want to use v2.
	suppress_warnings (bool) (optional): If this is set to True, You won't get any console warnings. This does not suppress errors.


	Methods 
	-------

	async get_ai_response(message: str, plan: str = '', **kwargs): Get random AI response.
	async get_image(type: str = 'any'): Get random image.
	async get_joke(type: str = 'any'): Get random joke.
	async close(): Closes the _session.
	
	"""
	def __init__(self, api_key: str, version: str = '4', suppress_warnings: bool = False):
		super().__init__(api_key, version, suppress_warnings)
		self._session = aiohttp.ClientSession(headers={'x-api-key': self.api_key})


	async def get_ai_response(self, 
		message:str, 
		plan:str='', 
		**kwargs) -> AIResponse:
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

		if self.version == '3':
			params = {
				'message': message, 
				'lang': kwargs.get('lang', 'en'), 
				'type': kwargs.get('type', 'stable'), 
				'bot_name': kwargs.get('bot_name', 'RSA'), 
				'dev_name': kwargs.get('dev_name', 'PGamerX'),
				'unique_id': kwargs.get('unique_id', ''),
			}
			if plan == '':
				response = await self._session.get(f'{self._base_url}/ai/response', params=params)
			else:
				response = await self._session.get(f'{self._base_url}/{plan}/ai/response', params=params)

		elif self.version == '4':
			params = {
				'message': message, 
				'server': kwargs.get('server', 'primary'), 
				'master': kwargs.get('master', 'PGamerX'), 
				'bot': kwargs.get('bot', 'RSA'), 
				'uid': kwargs.get('uid', ''), 
				'language': kwargs.get('language', 'en'), 
			}

			if plan == '':
				response = await self._session.get(f'{self._base_url}/ai', params=params)
			else:
				response = await self._session.get(f'{self._base_url}/{plan}/ai', params=params)

		_check_status(response)
		
		return AIResponse(await response.json())

	

	async def get_joke(self, type: str = 'any') -> Joke:
		"""
		This function is a coroutine
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		Equivalent to `Client.get_joke`
		"""
		if self.version == '4':
			response = await self._session.get(f'{self._base_url}/joke', params={'type': type})
		elif self.version == '3':
			response = await self._session.get(f'{self._base_url}/joke/{type}')

		_check_status(response)

		return Joke(await response.json())

	async def get_image(self, type:str = 'any') -> str:
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

		if self.version == '3':
			response = await self._session.get(f'{self._base_url}/image/{type}')

		elif self.version == '4':
			response =  await self._session.get(f'{self._base_url}/image', params={'type': type})

		_check_status(response)
			
		return (await response.json())[0]

	async def get_waifu(self, plan:str, type:str):
		"""
		This function is a coroutine
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		Gets a random waifu pic (SFW)
		
		Parameters:
			type (str) : The type of waifu. Can be one from the table below:
			
			|:-------:|
			|  Types  |
			|:-------:|
			|  waifu  |
			|  neko   |
			| shinobu |
			| megumin |
			|  bully  |
			| cuddle  |
			|:-------:|

		Returns:	
			Waifu

		Raises:
			BadAPIKey: The API key was invalid.
			HTTPError: An error occured while connecting to API.

		"""
		if self.version == '3':
			raise InvalidVersion("Version 3 does not support this method.")
			return

		if not type in WAIFU_TYPES:
			raise InvalidType("Invalid waifu type provided")
			return

		if not plan in PLANS:
			raise InvalidPlanError("The plan provided is invalid.")

		response = await self._session.get(f"{self._base_url}/{plan}/waifu", params={'type': type})

		_check_status(response)

		return Waifu((await response.json())[0])

	async def close(self):
		"""
		This function is a coroutine
		----------------------------

		Closes a _session

		"""
		await self._session.close()
