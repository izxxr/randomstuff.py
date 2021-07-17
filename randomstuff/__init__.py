"""
RandomStuff.py
~~~~~~~~~~~~~~

An easy to use python API wrapper for Random Stuff API.

:copyright: 2021-present nerdguyahmad.
:licence: MIT. See LICENSE for more details.
"""

from .ai_response import *
from .client import *
from .constants import *
from .errors import *
from .joke import *
from .waifu import *
# To use randomstuff.utils module import it manually.

__title__ = 'randomstuff.py'
__summary__ = 'An easy to use and feature rich wrapper for Random Stuff API'
__uri__ = 'https://github.com/nerdguyahmad/randomstuff.py'
__email__ = 'nerdguyahmad.contact@gmail.com'
__author__ = 'nerdguyahmad'
__version__ = '1.6.0'
__license__ = 'MIT'
__copyright__ = '2021-present nerdguyahmad.'

def get_version():
	return __version__
