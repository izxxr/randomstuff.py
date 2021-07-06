# What I did in the PR

- Removed extra lines in setup.py
- Added new `UnsupportedOperation` error which is raised when `AsyncClient` class is used in a synchronous with statement

- Client class instructs you to use `AsyncClient` when used in a `async with` statement

- Fixed some Exception inheritence

  - `InvalidVersionError` now properly ineherits `ArgumentError`

--------------
