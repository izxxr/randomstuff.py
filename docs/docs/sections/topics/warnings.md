# Warnings

Warnings are what this library uses to warn the user about possible issues without interrupting the actual program. They are different then errors as they don't stop your program.

These are simply used to warn the user about certain threats or issues like, deprecation warnings, usage of blocking methods from package inside async enivornment etc.

## Suppressing warnings
Set `suppress_warnings` to `True` while initializing the client to disable warnings.
```py
randomstuff.Client(api_key=..., suppress_warnings=True)
```
