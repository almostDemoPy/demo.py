# Immutable Objects
Immutables are objects that cannot be changed or further modified after it has been declared. Such example is a ` str `, ` int `, ` bool `, and ` tuple ` data type. These do not support item assignment.

```py
sample_string : str = "hello world"
sample_tuple : Tuple[int] = 1, 2, 3
sample_int : int = 123

>>> sample_string[4] = "s"
TypeError: 'string' object does not support item assignment

>>> sample_tuple[2] = 4
TypeError: 'tuple' object does not support item assignment

>>> sample_int[2] = 4
TypeError: 'int' object does not support item assignment
```

Booleans are immutable objects because they are a subclass of ` int `. Thus, they inherit the parent's immutability.

```py
>>> issubclass(bool, int)
True

>>> isinstance(True, int)
True
```