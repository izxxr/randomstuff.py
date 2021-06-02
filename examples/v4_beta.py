"""
Randomstuff.py wraps the current beta version of v4. 
The beta version only includes the ai response endpoint.

[ It is recommended NOT to use beta yet as it is unstable wait a few days. ]

There's a seperate method to use the beta mainly because the new beta has entirely different parameters.
"""
import randomstuff

client = randomstuff.Client(key='key', version="4")  # Initialize your Client instance with version "4"

response = client.get_ai_response_beta('Hi') # The new method. For more information, Read the beta page in wiki.
