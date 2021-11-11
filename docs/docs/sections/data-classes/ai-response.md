# AIResponse

Represents the response returned in `Client.get_ai_response()` method.

!!! warning "Version specific attributes"
    Attributes of this class are version specific. Except `message` attribute, all attributes are version specific.

=== "Attributes"
    | Name        | Description                                  | Type            | 
    | :---------- | :------------------------------------------- | :-------------- |
    | `message`   | The message on which response is required    | `str`           |
    | `plan`      | The plan to use. Must be one from [Plans](../topics/lists.md#plans).     | Optional[`str`] |
    | `language`  | The language of response. Default is English.| Optional[`str`] |
    | `server`    | The [AI server](../topics/lists.md#ai-servers) to use. Default is `primary`.  | Optional[`str`] |
    | `master`    | The bot's master AKA creator, This is used in responses. | Optional[`str`] |
    | `bot`    | The bot's name, This is used in responses. | Optional[`str`] |
    | `uid`    | The [Unique ID](../topics/unique-id.md) to use. | Optional[`str`] |
