# Boolean
A boolean value can be used in conditional statements or when setting or updating a value.

## False
A boolean value that denotes something that is not ` True `. This value can be created when a ` 0 ` or an empty string is passed in ` bool() ` built-in method, or of a conditional statement.

```py
>>> bool(0)
False

>>> bool("")
False

>>> 1 > 2
False

>>> not True
False
```


## True
A boolean value that denotes something that is not ` False `. Can be created when a non-empty string or array, or non-zero integer, or of a conditional statement is passed to the ` bool() ` built-in function.

```py
>>> bool(1)
True

>>> bool("Python")
True

>>> bool([1, 2, 3])
True

>>> 1 in [1, 2, 3]
True

>>> not False
True
```