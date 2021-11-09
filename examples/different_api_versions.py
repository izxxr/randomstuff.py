"""This example shows how to switch to a different versions of API"""

"""Randomstuff.py supports both v3 and v4 so you can use any version without any issues.

Warning! We don't recommend the use of V3 anymore! v4 is the latest and supported version! Please use v4 for general usage!

If you have a program running the API version 3, Please read migration guide on our documentation.
"""
import randomstuff

with randomstuff.Client(
    key="api-key-here", version="4"
) as client:  # Pass in API version in version argument. Choose one from 2 or 3 or 4 (v4 is beta).

    """Put your rest of code here. You have to change nothing when changing API versions. Wrapper deals with that itself."""
    ...
