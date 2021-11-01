# Frequently Asked Question
These are some questions that you might have, If your question is not here, Join our discord server and ask there. [Click here](https://api-info.pgamerx.com/discord) to join.

### Where can I get the API key?
[https://api-info.pgamerx.com/register](https://api-info.pgamerx.com/register) | Steps are pretty straight forward.

### What version of API should I be using?
The latest version is always the best. Currently latest version is version 4. To use the latest version, Simply remove `version` kwarg from your Client instance.

### Why do I get `PlanNotAllowed` error on `get_joke()`, `get_image()` etc. method when I have a plan?
Plans are only supported in following methods:

- `get_ai_response()`
- `get_waifu()`

To use the other methods, You will have to use normal API key (API key with no plan).

### Why can't I change attributes of an object?
All objects are frozen dataclasses meaning their attributes cannot be changed.

### What is unique ID?
Please see the [Unique ID](unique-id.md) page.
