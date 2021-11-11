"""
RandomStuff.py
~~~~~~~~~~~~~~

A python API wrapper around Random Stuff API.

:copyright: 2021-present nerdguyahmad.
:licence: MIT. See LICENSE for more details.
"""

from .ai_response import *
from .client import *
from .constants import *
from .errors import *
from .joke import *
from .waifu import *
from .covid import *
from . import utils

__title__ = 'randomstuff.py'
__summary__ = 'An python API wrapper around Random Stuff API'
__uri__ = 'https://github.com/nerdguyahmad/randomstuff.py'
__email__ = 'nerdguyahmad.contact@gmail.com'
__author__ = 'nerdguyahmad'
__version__ = '2.5.0a'
__license__ = 'MIT'
__copyright__ = '2021-present nerdguyahmad.'

def get_version():
    return __version__
