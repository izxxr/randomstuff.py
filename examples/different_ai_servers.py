"""
You can change the get_ai_response server to primary, backup and unstable.

Warning! Use primary for general and backup if primary is down. unstable will have problems
"""
import randomstuff

client= randomstuff.Client(key="api-key-here")
client.get_ai_response(message="Hi", server="primary") # Pass in type in server argument. Choose from `primary`, `backup` and `unstable`.
