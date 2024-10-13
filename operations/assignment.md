# Assignment
Assignment operators, are another way of, allows the declaration and defining of variables. Basic assignment operation is with the ` = ` assignment operator:
```py
variable = "some value"

>>> variable
"some value"
```


## Add AND Operation
Adds both the operands and assigns the new value to the left operand

**Equivalent to**:
```py
x = y
x = x + z
```

**Example**
```py
x : int = 0
x += 3

>>> x
3
```


## Bitwise-AND AND Operation
Performs the ` & ` bitwise-AND to both operands and assigns the new value to the left operand

**Equivalent to**:
```py
x = y
x = x & z
```

**Example**
```py
x : int = 13
x &= 5

>>> x
5
```


## Bitwise Left Shift AND Operation
Performs the ` << ` bitwise left shift operation to both operands and assigns the new value to the left operand

**Equivalent to**:
```py
x = y
x = x << z
```

**Example**
```py
x : int = 2
x <<= 3

>>> x
16
```


## Bitwise-OR AND Operation
Performs the ` | ` bitwise-OR on both operands and assigns the new value to the left operand

**Equivalent to**:
```py
x = y
x = x | z
```

**Example**
```py
x : int = 10
x |= 5

>>> x
15
```


## Bitwise Right Shift AND Operation
Performs the ` >> ` bitwise right shift on both operands and assigns the new value to the left operand

**Equivalent to**:
```py
x = y
x = x | z
```

**Example**
```py
x : int = 10
x >>= 2

>>> x
2
```


## Bitwise-xOR AND Operation
Performs the ` ^ ` bitwise-xOR on both operands and assigns the new value to the left operand

**Equivalent to**:
```py
x = y
x = x ^ z
```

**Example**
```py
x : int = 10
x ^= 5

>>> x
15
```


## Divide Float AND Operation
Divides both operands that returns an ` float ` and assigns the new value to the left operand

**Equivalent to**:
```py
x = y
x = x / z
```

**Example**
```py
x : int = 10
x /= 5

>>> x
2.0
```


## Divide Floor AND Operation
Divides both operands that returns an ` int ` and assigns the new value to the left operand

**Equivalent to**:
```py
x = y
x = x // z
```

**Example**
```py
x : int = 10
x //= 5

>>> x
2
```


## Exponent AND Operation
Calculates the exponent of on both operands and assigns the new value to the left operand

**Equivalent to**:
```py
x = y
x = x ** z
```

**Example**
```py
x : int = 10
x **= 2

>>> x
100
```


## Modulo AND Operation
Calculates the remainder on both operands and assigns the new value to the left operand

**Equivalent to**:
```py
x = y
x = x % z
```

**Example**
```py
x : int = 10
x %= 3

>>> x
1
```


## Multiply AND Operation
Multiplies both operands and assigns the new value to the left operand

**Equivalent to**:
```py
x = y
x = x * z
```

**Example**
```py
x : int = 10
x *= 5

>>> x
50
```


## Subtract AND Operation
Subtracts both operands and assigns the new value to the left operand

**Equivalent to**:
```py
x = y
x = x - z
```

**Example**
```py
x : int = 10
x -= 5

>>> x
5
```