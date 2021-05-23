"""This example is for the users that have bought one of the paid plans for AI response endpoint"""

"""
RandomStuff.py supports all type of plans for AI response endpoint. 
"""
import randomstuff

client = randomstuff.Client(key="api-key-here") # Input the API key that has the paid plan. Please note that you cannot use plans with version 2 of API!

"""Below are examples for all the plans choose the one for the plan you have"""

response = client.get_ai_response(message="The message", plan=None) # No plan (Normal aka Free)
print(response)

response = client.get_ai_response(message="The message", plan="pro") # Pro plan
print(response)

response = client.get_ai_response(message="The message", plan="ultra") # Ultra plan
print(response)

response = client.get_ai_response(message="The message", plan="biz") # Biz plan
print(response)

response = client.get_ai_response(message="The message", plan="mega") # Mega plan
print(response)
