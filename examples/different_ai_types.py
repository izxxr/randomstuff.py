"""
You can change the get_ai_response type to stable and unstable.

Warning! Use stable for general use as the name suggests, unstable is unstable and will have problems
"""
import randomstuff

client= randomstuff.Client(key="api-key-here")
client.get_ai_response(message="Hi", type="stable") # Pass in type in type argument. Choose from `stable` and `unstable`
