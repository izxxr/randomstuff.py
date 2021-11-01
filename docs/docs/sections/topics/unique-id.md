# Unique ID

Unique ID is part of AI response endpoint. It is used to create a new session for a specific user. What does that mean? Read next.

## What does "session" means?
So, when you create a new session with an unique ID, It actually stores your data you tell the bot in that ID so bot will remember your name etc. You can use the ID later and bot will remember you.

!!! info "Information"
    If you don't provide a unique ID, It will store the info globally in your API key instead.

The unique ID can be anything, you should use secure unique IDs. Use `utils.generate_unique_id()` method to create a strong unique ID.


## Example
```py
import randomstuff

client = randomstuff.Client(api_key="api-key")
response = client.get_ai_response("What is my name?", 
    uid="a very unique id",
)
print(response.message)
```

The bot will respond with something like "What is your name?" and then when you will tell your name, it will remember it in ID: `a very unique id`. It will remember all the things you tell until you change the ID.