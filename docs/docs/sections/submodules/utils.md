# `randomstuff.utils`
`randomstuff.utils` is a sub module that contains some useful functions to aid with some common tasks.

!!! info "Usage"
    To use this module, You have to state `utils` before functions. For example,
    ```py
    >> randomstuff.utils.generate_unique_id()
    ``` 

## Methods

### **`generate_unique_id(level: Optional[int] =30)`**
A helper function that generates a complex key to use as unique ID.

=== "Parameters"
    | Name        | Description                                  | Type | 
    | :---------- | :------------------------------------------- | :--- |
    | **`level`**     | Number of characters the string should have  | Optional[**`int`**]     |

=== "Returns"
    `str` : The generated string.
