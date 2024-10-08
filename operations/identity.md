# Identity

## Is-Not Operation
Returns ` True ` if both operands are not identical in memory to each other

**Example**
```py
a : int = 10
b : int = a

>>> a is not b
False

a : int = 10
b : int = 10

>>> a is not b
False

a : int = 10
b : int = 20

>>> a is not b
True
```


## Is Operation
Returns ` True ` if both operands are identical in memory

**Example**
```py
a : int = 10
b : int = 10

>>> a is b
True

a : int = 10
b : int = a

>>> a is b
True

a : int = 10
b : int = 20

>>> a is b
False
```