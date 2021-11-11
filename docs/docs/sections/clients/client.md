# `randomstuff.Client`

The main client class to make API calls.

!!! warning "Non-async class"
    All functions in this class are blocking meaning they are not suitable for async programs like Discord bots etc. Please have a look at [`AsyncClient`](async-client.md)

=== "Parameters/Attributes"
    
    * ### **`api_key`**

        **Type:** `str`

        Your API authentication key.
    
    * ### **`version`**

        **Type:** Optional[`str`]

        The version of API to use, This cannot be changed after initalisation. Defaults to "4".

    * ### **`suppress_warnings`**

        **Type:** Optional[`bool`]

        Whether or not to suppress warnings like deprecated versions, etc. Defaults to `False`.

=== "Methods"
    
    * ### **`get_ai_response(message: str, plan: str = '', **kwargs)`**

        Gets the AI response to provided message.

        !!! warning "Version-specific parameters"
            This method takes version specific parameters. Version 3 parameters differ from version 4 parameters. All parameters except `message` and `plan` are keyword arguments.

        === "Parameters (Version 4)"
            | Name        | Description                                  | Type            | 
            | :---------- | :------------------------------------------- | :-------------- |
            | `message`   | The message on which response is required    | `str`           |
            | `plan`      | The plan to use. Must be one from [Plans](../topics/lists.md#plans).     | Optional[`str`] |
            | `language`  | The language of response. Default is English.| Optional[`str`] |
            | `server`    | The [AI server](../topics/lists.md#ai-servers) to use. Default is `primary`.  | Optional[`str`] |
            | `master`    | The bot's master AKA creator, This is used in responses. | Optional[`str`] |
            | `bot`    | The bot's name, This is used in responses. | Optional[`str`] |
            | `uid`    | The [Unique ID](../topics/unique-id.md) to use. | Optional[`str`] |


        === "Parameters (Version 3)"
            | Name        | Description                                  | Type            | 
            | :---------- | :------------------------------------------- | :-------------- |
            | `message`   | The message on which response is required    | `str`           |
            | `plan`      | The plan to use. Must be one from [Plans](../topics/lists.md#plans).     | Optional[`str`] |
            | `lang`  | The language of response. Default is English.| Optional[`str`] |
            | `type`    | The type of AI response. Either `stable` or `unstable`  | Optional[`str`] |
            | `dev_name`    | The bot's dev AKA creator, This is used in responses. | Optional[`str`] |
            | `bot_name`    | The bot's name, This is used in responses. | Optional[`str`] |
            | `unqiue_id`    | The [Unique ID](../topics/unique-id.md) to use. | Optional[`str`] |

        === "Returns"
            - [`AIResponse`](../data-classes/ai-response.md) : The obtained response.

    * ### **`get_image(type: str = 'any')`**

        Gets random image of provided type.

        === "Parameters"
            | Name        | Description                                  | Type            | 
            | :---------- | :------------------------------------------- | :-------------- |
            | `type`      | One of [types of image](../topics/lists.md#image-types).  Defaults to `any`  | `str`           |
            
        === "Returns"
            - `str` : The URL of image.

    * ### **`get_joke(type: str = 'any')`**

        Gets random joke.

        !!! tip "Tip"
            Use `Client.get_safe_joke()` method to filter unsafe jokes.

        === "Parameters"
            | Name        | Description                                  | Type            | 
            | :---------- | :------------------------------------------- | :-------------- |
            | `type`      | One of [types of jokes](../topics/lists.md#joke-types).  Defaults to `any`  | `str`           |
            
        === "Returns"
            - `Joke` : The obtained Joke.

    * ### **`get_safe_joke(type: str = 'any')`**

        Filters any unsafe jokes.

        === "Parameters"
            | Name        | Description                                  | Type            | 
            | :---------- | :------------------------------------------- | :-------------- |
            | `type`      | One of [types of jokes](../topics/lists.md#joke-types).  Defaults to `any`  | `str`           |
            
        === "Returns"
            - `Joke` : The obtained **safe** Joke.

    * ### **`get_waifu(plan: str, type: str = 'any')`**

        Gets random anime image.

        !!! warning "Plan required"
            This method requires pro or higher plan.

        === "Parameters"
            | Name        | Description                                  | Type            | 
            | :---------- | :------------------------------------------- | :-------------- |
            | `type`      | One of [types of waifus](../topics/lists.md#anime-types).  Defaults to `any`  | `str`           |
            
        === "Returns"
            - `str` : The URL of image.

    


    * ### **`get_weather(city: str)`**

        Gets weather of provided city.

        === "Parameters"
            | Name        | Description                                  | Type            | 
            | :---------- | :------------------------------------------- | :-------------- |
            | `city`      | The name of city.                            | `str`           |
            
        === "Returns"
            - `Weather` : The weather of provided city.

    * ### **`close()`**

        Closes a session.

        !!! tip "Tip"
            If you use legacy method instead of context manager, This method is recommended to be used after usage. If you use context manager, Library closes the session automatically internally so it is not needed while using context manager.

            ```py
            with Client(...) as client:
                # do things here
            ``` 
            as soon as with block ends, The session is closed.
