from .errors import *
from .constants import *
from .covid import *
from .ai_response import *
from .joke import *
from .waifu import *
from .weather import *
from ._helper import _check_coro, _check_status, _warn
from . import utils
from typing import Optional
import aiohttp
import inspect
import requests
import random

class BaseClient:
    """Represents the base of both synchronus and asynchronous clients.

    This is an internal class and is not meant to be used.
    """

    def __init__(self, 
        api_key: str, 
        version: Optional[str] = '5', 
        suppress_warnings: Optional[bool] = False):

        if version in DISCONTINUED_VERSIONS:
            raise DeprecationWarning(f"v{version} has been discontinued. Please use v{VERSIONS[-1]}")
            return

        if not version in VERSIONS:
            raise InvalidVersionError("Invalid API version was provided.")
            return

        self.version = version
        self.api_key = api_key
        self.suppress_warnings = suppress_warnings
        self._base_url = f"{BASE_URL}/v{self.version}"
        self._randomised_uid = utils.generate_uid()

        if self.version != VERSIONS[-1]:
            _warn(self, f'Latest version of API is v{VERSIONS[-1]} but you are using v{self.version}.\n')
    
    def _resolve_ai_params(self, message:str, plan:str = '', **kwargs):
        if not plan in PLANS:
            raise InvalidPlanError(F"Invalid Plan. Choose from {PLANS}")
            return

        if self.version == '4':
            if not kwargs.get('server', 'primary') in SERVERS_V4:
                raise InvalidServerError(f"Invalid server type Must be one from {SERVERS_V3}.") 
                return

        if self.version == '5':
            if not kwargs.get('server', 'main') in SERVERS_V5:
                raise InvalidServerError(f"Invalid server type choose from {SERVERS_V4}.") 
                return

        if self.version == '3':
            params = {
                'message': message, 
                'lang': kwargs.get('lang', 'en'), 
                'type': kwargs.get('type', 'stable'), 
                'bot_name': kwargs.get('bot_name', 'RSA'), 
                'dev_name': kwargs.get('dev_name', 'PGamerX'),
                'unique_id': kwargs.get('unique_id', self._randomised_uid),
            }
            
        elif self.version == '4':
            params = {
                'message': message, 
                'server': kwargs.get('server', 'primary'), 
                'master': kwargs.get('master', 'PGamerX'), 
                'bot': kwargs.get('bot', 'RSA'), 
                'uid': kwargs.get('uid', self._randomised_uid), 
                'language': kwargs.get('language', 'en')
            }

            if plan == '':
                response = self._session.get(f'{self._base_url}/ai', params=params)
            else:
                response = self._session.get(f'{self._base_url}/{plan}/ai', params=params)

        elif self.version == '5':
            params = {
                'message': message,
                'server': kwargs.get('server', 'main'),
                'uid': kwargs.get('uid', self._randomised_uid),
                'bot_name': kwargs.get('name', 'Random Stuff API'),
                'bot_master': kwargs.get('master', 'PGamerX'),
                'bot_gender': kwargs.get('gender', 'Male'),
                'bot_age': kwargs.get('age', '19'),
                'bot_company': kwargs.get('company', 'PGamerX Studio'),
                'bot_location': kwargs.get('location', 'India'),
                'bot_email': kwargs.get('email', 'admin@pgamerx.com'),
                'bot_build': kwargs.get('build', 'Public'),
                'bot_birth_year': kwargs.get('birth_year', '2002'),
                'bot_birth_date': kwargs.get('birth_year', '1st January 2002'),
                'bot_birth_place': kwargs.get('birth_place', 'India'),
                'bot_favorite_color': kwargs.get('favorite_color', 'Blue'),
                'bot_favorite_book': kwargs.get('favorite_book', 'Harry Potter'),
                'bot_favorite_band': kwargs.get('favorite_band', 'Imagine Doggos'),
                'bot_favorite_artist': kwargs.get('favorite_artist', 'Eminem'),
                'bot_favorite_actress': kwargs.get('favorite_actress', 'Emma Watson'),
                'bot_favorite_actor': kwargs.get('favorite_actor', 'Jim Carrey')
            }

        if self.version == '3':
            url = f"{self._base_url}/{plan+'/' if plan else ''}ai/response"
        elif self.version == '4':
            url = f"{self._base_url}/{plan+'/' if plan else ''}/ai"
        elif self.version == '5':
            url = f"{self._base_url}/{'premium/'+plan+'/' if plan else ''}/ai"

        return params, url


class Client(BaseClient):
    """Represent a synchronounus client
    
    Parameters
    ----------
      api_key : str
        Your API authentication key.

      version : Optional[str]
        The version number of API. It is 4 by default. Set it to 3 if you want to use v3.
      
      plan : Optional[str]
        The plan to use. You must have a plan assigned to your API key.

      suppress_warnings Optional[bool]: 
        If this is set to True, You won't get any console warnings. This does not suppress errors.
        
    Basic Example
    -------------

    import randomstuff

    with randomstuff.Client(api_key='Your API key here') as client:
        response = client.get_ai_response('Hi')
        print(response.message)

    """
    def __init__(self, api_key: str, version: Optional[str] = '5', plan: Optional[str] = None, suppress_warnings: Optional[bool] = False):
        super().__init__(
            api_key=api_key,
            version=version,
            suppress_warnings=suppress_warnings
            )
        self._session = requests.Session()

        if self.version == '5':
            self._session.headers.update({'Authorization': self.api_key})
        else:
            self._session.headers.update({'x-api-key': self.api_key})

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, tb):
        self._session.close()
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self._session.close()

    def get_ai_response(self, 
        message:str, 
        plan:str='', 
        **kwargs) -> AIResponse:
        """Gets AI response from the API.

        This method has version based parameters
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        Common parameters:
            message (str) : The message to which response is required.
            plan (optional) (str) : The plan to use. This is optional and can only be used if API key has a paid plan registered.

            Above two parameters are not version specific they are supported in all versions.

        Version 3 specific:
            lang (optional) (str) : Language in which response is required. Defaults to `en`.
            type (optional) (str) : Type of response. Can be `stable` or `unstable`
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
        
        Version 5 specific:
            uid (optional) (str) : The session specific user ID. Use this to make sessions for
                                   certain user.
            server: The server from which the response should be obtained, Can be either `main` or `backup`

            Customisation parameters:
                - bot_name
                - bot_master
                - bot_gender
                - bot_age
                - bot_company
                - bot_location
                - bot_email
                - bot_build
                - bot_birth_year
                - bot_birth_date
                - bot_birth_place
                - bot_favorite_color
                - bot_favorite_book
                - bot_favorite_band
                - bot_favorite_artist
                - bot_favorite_actress
                - bot_favorite_actor

                All these parameters are used for customistation of responses. They are
                all optional and their default values can be found at:
                https://docs.pgamerx.com/endpoints/ai#customisation

        Returns: Response as an AIResponse object.
        """
        _check_coro(self)
        params, url = self._resolve_ai_params(message, plan, **kwargs)

        response = self._session.get(url, params=params)
        _check_status(response)
        response = response.json()

        if self.version == '3':
            return AIResponse(
                message=response[0].get('message'),
                response=response[0].get('message'),
                api_key=response[0].get('api_key'),
                success=response[0].get('success'),
                )
        elif self.version == '4':
            return AIResponse(
                message=response[0].get('message'),
                response=response[0].get('message'),
                response_time=response[1].get('response_time'),
                success=True,
                uid=params.get('uid'),
                server=params.get('server')
                )
        elif self.version == '5':
            return AIResponse(
                message=response[0].get('response'),
                response=response[0].get('response'),
                success=True,
                uid=params.get('uid'),
                server=params.get('server')
                )
        


    
    def get_image(self, type: str = 'any') -> str:
        """Gets an image

        Parameters:
            type (str) (optional): The type of image. By default, it is 'any'.

        Returns:
            str: Link of image
        """
        if type == 'any':
            type = random.choice(IMAGE_TYPES)

        if not type in IMAGE_TYPES:
            raise InvalidType('Invalid image type provided.')
            return

        _check_coro(self)

        if self.version == '3':
            response = self._session.get(f'{self._base_url}/image/{type}')

        elif self.version in ['4', '5']:
            response = self._session.get(f'{self._base_url}/image', params={'type': type})

        _check_status(response)

        return response.json()[0]

    def get_joke(self, type: str = 'any', blacklist: list = []) -> Joke:
        """Gets a joke

        Parameters:
            type : Optional[str]
                The type of joke. By default, it is 'any'.
           
            blacklist : Optional[JokeFlags]
                The list of flags to blacklist. You can provide the list of flags that you
                don't want to be True in returned jokes. Useful to get SFW jokes only.

        Returns:
            randomstuff.Joke: The `randomstuff.Joke` object for the joke.
        """

        if not type in JOKE_TYPES:
            raise InvalidType('Invalid Joke type provided.')
            return

        if self.version in ['3', '4'] and blacklist:
            raise InvalidVersionError('blacklisting of flags is only supported on version 5.')

        _check_coro(self)

        if self.version == '4':
            response = self._session.get(f'{self._base_url}/joke', params={'type': type})
        
        elif self.version == '3':
            response = self._session.get(f'{self._base_url}/joke/{type}')

        elif self.version == '5':
            blist = ''
            if blacklist:
                blist = ','.join(blacklist)

            response = self._session.get(f'{self._base_url}/premium/joke', params={'type': type, 'blacklist': blist})            

        _check_status(response)

        response = response.json()

        return Joke(
            category=response.get('category'),
            type=response.get('type'),
            joke=response.get('joke') if response.get('joke') else {'setup': response.get('setup'), 'delivery': response.get('delivery')},
            flags=JokeFlags(**response.get('flags')),
            id=response.get('id'),
            safe=response.get('safe'),
            lang=response.get('lang')
            )


    def get_waifu(self, plan: str, type: str = 'any') -> Waifu:
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

            or setting it to `any` will return any type of above.

        Returns:    
            Waifu

        Raises:
            BadAPIKey: The API key was invalid.
            HTTPError: An error occured while connecting to API.

        """
        if type == 'any':
            type = random.choice(WAIFU_TYPES)

        if self.version == '3':
            raise InvalidVersionError("Version 3 does not support this method.")
            return

        if not type in WAIFU_TYPES:
            raise InvalidType("Invalid waifu type provided")
            return

        if not plan in PLANS:
            raise InvalidPlanError("The plan provided is invalid.")

        _check_coro(self)

        if self.version == '4':
            response = self._session.get(f"{self._base_url}/{plan}/waifu", params={'type': type})
        elif self.version == '5':
            response = self._session.get(f"{self._base_url}/premium/{plan}/waifu", params={'type': type})

        _check_status(response)

        return Waifu(url=response.json()[0]['url'])

    def get_weather(self, city: str) -> Weather:
        '''
        Gets the weather of provided city.

        Parameters:

          city : str 
            The city of which weather should be returned.

        Returns:
          The weather of the provided city.

        Return Type:
          Weather

        Raises:
          InvalidCityError : The city provided is invalid or not found.
        '''
        if self.version == '3':
            raise InvalidVersionError("Version 3 does not support this method.")
            return

        response = self._session.get(f"{self._base_url}/weather", params={'city': city})

        _check_status(response)
        response = response.json()

        if response[0].get('error') is True:
            raise InvalidCityError(response[0].get('message'))

        return Weather(
            location=WeatherLocation(**response[0].get('location', {})),
            current=CurrentWeather(**response[0].get('current', {})),
            forecast=[WeatherForecast(**forecast) for forecast in response[0].get('forecast')]
            )

    def get_covid_data(self, country: str = None):
        '''Get covid-19 data of provided country or entire world.

        Parameters:

            country : Optional[str]
                The country to get covid data of. This can be left unchanged to get data
                of entire world.

        Returns:
            Either ``GlobalCovidData`` or ``CountryCovidData`` instance. Note that the global
            data doesn't has a country attribute and it is different from Country data as it has some
            additional attributes like ``condition`` and ``active_cases`` which are not in Country data
            Also in global data, all cases attributes are ``str`` instead of being Cases object like 
            country data.
        '''
        if self.version in ['4', '3']:
            raise InvalidVersionError(f"Version {self.version} does not support this method.")
            return

        response = self._session.get(f'{self._base_url}/covid', params={'country': country})
        _check_status(response)
        response = response.json()

        if country is None:
            return GlobalCovidData(
                total_cases=response.get('totalCases'),
                total_deaths=response.get('totalDeaths'),
                total_recovered=response.get('totalRecovered'),
                active_cases=response.get('activeCases'),
                closed_cases=response.get('closedCases'),
                condition=CovidCondition(
                    mild=response.get('condition')['mild'],
                    critical=response.get('condition')['critical'],
                    )
                )

        return CountryCovidData(
            country=Country(
                name=response.get('country')['name'],
                flag_img=response.get('country')['flagImg']
                ),
            cases=Cases(
                total=response.get('cases')['total'],
                recovered=response.get('cases')['recovered'],
                deaths=response.get('cases')['deaths'],
                ),
            closed_cases=ClosedCases(
                total=response.get('closedCases')['total'],
                percentage=ClosedCasesPercentage(
                    death=response.get('closedCases')['percentage']['death'],
                    discharge=response.get('closedCases')['percentage']['discharge']
                    ),
                )
            )

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
    def __init__(sself, api_key: str, version: Optional[str] = '5', plan: Optional[str] = None, suppress_warnings: Optional[bool] = False):
        super().__init__(
            api_key=api_key,
            version=version,
            suppress_warnings=suppress_warnings
            )
        self._session = aiohttp.ClientSession()
        
        if self.version == '5':
            self._session.headers.update({'Authorization': self.api_key})
        else:
            self._session.headers.update({'x-api-key': self.api_key})
    
    async def _resolve_ai_params(self, message:str, plan:str = '', **kwargs):
        if not plan in PLANS:
            raise InvalidPlanError(F"Invalid Plan. Choose from {PLANS}")
            return

        if self.version == '4':
            if not kwargs.get('server', 'primary') in SERVERS_V4:
                raise InvalidServerError(f"Invalid server type Must be one from {SERVERS_V3}.") 
                return

        if self.version == '5':
            if not kwargs.get('server', 'main') in SERVERS_V5:
                raise InvalidServerError(f"Invalid server type choose from {SERVERS_V4}.") 
                return

        if self.version == '3':
            params = {
                'message': message, 
                'lang': kwargs.get('lang', 'en'), 
                'type': kwargs.get('type', 'stable'), 
                'bot_name': kwargs.get('bot_name', 'RSA'), 
                'dev_name': kwargs.get('dev_name', 'PGamerX'),
                'unique_id': kwargs.get('unique_id', self._randomised_uid),
            }
            
        elif self.version == '4':
            params = {
                'message': message, 
                'server': kwargs.get('server', 'primary'), 
                'master': kwargs.get('master', 'PGamerX'), 
                'bot': kwargs.get('bot', 'RSA'), 
                'uid': kwargs.get('uid', self._randomised_uid), 
                'language': kwargs.get('language', 'en')
            }

            if plan == '':
                response = self._session.get(f'{self._base_url}/ai', params=params)
            else:
                response = self._session.get(f'{self._base_url}/{plan}/ai', params=params)

        elif self.version == '5':
            params = {
                'message': message,
                'server': kwargs.get('server', 'main'),
                'uid': kwargs.get('uid', self._randomised_uid),
                'bot_name': kwargs.get('name', 'Random Stuff API'),
                'bot_master': kwargs.get('master', 'PGamerX'),
                'bot_gender': kwargs.get('gender', 'Male'),
                'bot_age': kwargs.get('age', '19'),
                'bot_company': kwargs.get('company', 'PGamerX Studio'),
                'bot_location': kwargs.get('location', 'India'),
                'bot_email': kwargs.get('email', 'admin@pgamerx.com'),
                'bot_build': kwargs.get('build', 'Public'),
                'bot_birth_year': kwargs.get('birth_year', '2002'),
                'bot_birth_date': kwargs.get('birth_year', '1st January 2002'),
                'bot_birth_place': kwargs.get('birth_place', 'India'),
                'bot_favorite_color': kwargs.get('favorite_color', 'Blue'),
                'bot_favorite_book': kwargs.get('favorite_book', 'Harry Potter'),
                'bot_favorite_band': kwargs.get('favorite_band', 'Imagine Doggos'),
                'bot_favorite_artist': kwargs.get('favorite_artist', 'Eminem'),
                'bot_favorite_actress': kwargs.get('favorite_actress', 'Emma Watson'),
                'bot_favorite_actor': kwargs.get('favorite_actor', 'Jim Carrey')
            }

        if self.version == '3':
            url = f"{self._base_url}/{plan+'/' if plan else ''}ai/response"
        elif self.version == '4':
            url = f"{self._base_url}/{plan+'/' if plan else ''}/ai"
        elif self.version == '5':
            url = f"{self._base_url}/{'premium/'+plan+'/' if plan else ''}/ai"

        return params, url
    
    
    async def __aenter__(self):
        return self
        
    async def __aexit__(self, exc_type, exc_value, tb):
        await self._session.close()

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, tb):
        raise UnsupportedOperation("Could not close the client session. Please use \"async with\" instead\n")


    async def get_ai_response(self, 
        message:str, 
        plan:str='', 
        **kwargs) -> AIResponse:
        """
        This function is a coroutine
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        Equivalent to `Client.get_ai_response`
        """

        _check_coro(self)
        params, url = await self._resolve_ai_params(message, plan, **kwargs)

        response = await self._session.get(url, params=params)
        _check_status(response)
        response = await response.json()

        if self.version == '3':
            obj = AIResponse(
                message=response[0].get('message'),
                response=response[0].get('message'),
                api_key=response[0].get('api_key'),
                success=response[0].get('success'),
                )
        elif self.version == '4':
            obj = AIResponse(
                message=response[0].get('message'),
                response=response[0].get('message'),
                response_time=response[1].get('response_time'),
                success=True,
                uid=params.get('uid'),
                server=params.get('server')
                )
        elif self.version == '5':
            obj = AIResponse(
                message=response[0].get('response'),
                response=response[0].get('response'),
                success=True,
                uid=params.get('uid'),
                server=params.get('server')
                )

        return obj

    

    async def get_joke(self, type: str = 'any', blacklist: list = []) -> Joke:
        """
        This function is a coroutine
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        Equivalent to `Client.get_joke`
        """
        if not type in JOKE_TYPES:
            raise InvalidType('Invalid Joke type provided.')
            return

        if self.version in ['3', '4'] and blacklist:
            raise InvalidVersionError('blacklisting of flags is only supported on version 5.')
        
        _check_coro(self)

        if self.version == '4':
            response = await self._session.get(f'{self._base_url}/joke', params={'type': type})
        
        elif self.version == '3':
            response = await self._session.get(f'{self._base_url}/joke/{type}')

        elif self.version == '5':
            blist = ''
            if blacklist:
                blist = ','.join(blacklist)

            response = await self._session.get(f'{self._base_url}/premium/joke', params={'type': type, 'blacklist': blist})            

        _check_status(response)

        response = await response.json()
        
        return Joke(
            category=response.get('category'),
            type=response.get('type'),
            joke=response.get('joke') if response.get('joke') else {'setup': response.get('setup'), 'delivery': response.get('delivery')},
            flags=JokeFlags(**response.get('flags')),
            id=response.get('id'),
            safe=response.get('safe'),
            lang=response.get('lang')
            )

    async def get_image(self, type: str = 'any') -> str:
        """This function is a coroutine
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        Equivalent to `Client.get_image`
        """
        if type == 'any':
            type = random.choice(IMAGE_TYPES)

        if not type in IMAGE_TYPES:
            raise InvalidType('Invalid image type provided.')
            return

        _check_coro(self)

        if self.version == '3':
            response = await self._session.get(f'{self._base_url}/image/{type}')

        elif self.version in ['4', '5']:
            response = await self._session.get(f'{self._base_url}/image', params={'type': type})

        _check_status(response)

        return await response.json()[0]

    async def get_waifu(self, plan: str, type: str = 'any') -> Waifu:
        """
        This function is a coroutine
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        Equivalent to `Client.get_waifu`
        """
        if type == 'any':
            type = random.choice(WAIFU_TYPES)

        if self.version == '3':
            raise InvalidVersionError("Version 3 does not support this method.")
            return

        if not type in WAIFU_TYPES:
            raise InvalidType("Invalid waifu type provided")
            return

        if not plan in PLANS:
            raise InvalidPlanError("The plan provided is invalid.")

        _check_coro(self)

        if self.version == '4':
            response = await self._session.get(f"{self._base_url}/{plan}/waifu", params={'type': type})
        elif self.version == '5':
            response = await self._session.get(f"{self._base_url}/premium/{plan}/waifu", params={'type': type})

        _check_status(response)

        return Waifu(url=(await response.json()[0]['url']))

    async def get_weather(self, city: str) -> Weather:
        '''
        This function is a coroutine
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        Equivalent to `Client.get_weather`
        '''
        
        if self.version == '3':
            raise InvalidVersionError("Version 3 does not support this method.")
            return

        response = await self._session.get(f"{self._base_url}/weather", params={'city': city})

        _check_status(response)
        response = await response.json()

        if response[0].get('error') is True:
            raise InvalidCityError(response[0].get('message'))

        return Weather(
            location=WeatherLocation(**response[0].get('location', {})),
            current=CurrentWeather(**response[0].get('current', {})),
            forecast=[WeatherForecast(**forecast) for forecast in response[0].get('forecast')]
            )
    
    async def get_covid_data(self, country: str = None):
        '''This function is a coroutine
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        Equivalent to `Client.get_covid_data`
        '''
        if self.version in ['4', '3']:
            raise InvalidVersionError(f"Version {self.version} does not support this method.")
            return

        response = await self._session.get(f'{self._base_url}/covid', params={'country': country})
        _check_status(response)
        response = await response.json()

        if country is None:
            return GlobalCovidData(
                total_cases=response.get('totalCases'),
                total_deaths=response.get('totalDeaths'),
                total_recovered=response.get('totalRecovered'),
                active_cases=response.get('activeCases'),
                closed_cases=response.get('closedCases'),
                condition=CovidCondition(
                    mild=response.get('condition')['mild'],
                    critical=response.get('condition')['critical'],
                    )
                )

        return CountryCovidData(
            country=Country(
                name=response.get('country')['name'],
                flag_img=response.get('country')['flagImg']
                ),
            cases=Cases(
                total=response.get('cases')['total'],
                recovered=response.get('cases')['recovered'],
                deaths=response.get('cases')['deaths'],
                ),
            closed_cases=ClosedCases(
                total=response.get('closedCases')['total'],
                percentage=ClosedCasesPercentage(
                    death=response.get('closedCases')['percentage']['death'],
                    discharge=response.get('closedCases')['percentage']['discharge']
                    ),
                )
            )
    
    async def close(self):
        """
        This function is a coroutine
        ----------------------------

        Closes a _session

        """
        await self._session.close()
