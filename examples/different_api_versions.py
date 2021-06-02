"""This example shows how to switch to a different versions of API"""

"""Randomstuff.py supports both v2 and v3 so you can use any version without any issues.

Warning! We don't recommend the use of V2 anymore! v3 is the latest and supported version! Please use v3 for general usage!

If you have a program running the API version 2, You don't have to worry about changing your code, This wrapper deals with it for you.
"""
import randomstuff

client = randomstuff.Client(key="api-key-here", version="3") # Pass in API version in version argument. Choose one from 2 or 3 or 4 (v4 is beta).

"""Put your rest of code here. You have to change nothing when changing API versions. Wrapper deals with that itself."""
...
