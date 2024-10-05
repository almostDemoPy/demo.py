# Class
A class is a user-defined blueprint of an object. The class can be a subclass of an existing class.

A class can be created with the ` class ` keyword.

```py
class Sample: ...
```

The above example shows an example of creating a class named ` Sample `. Currently, the ` Sample ` class is just empty and does nothing yet.

Calling the class creates an instance of it. This calls the ` __new__ ` and ` __init__ ` dunder methods [ in order ] and returns an instance of it.

```py
class Sample: ...

sample = Sample()

>>> isinstance(sample, Sample)
True
```

` isinstance() ` built-in function allows us to check if an object is an instance of a class.

## Class and Instance Variables
Variables declared inside the class are called **Class Variables**, while those that are declared inside the class' ` __init__ ` dunder method are called **Instance Variables**, defined with a ` self ` prefix.

Declared class variables are attached to the class. Thus, these variables can be accessed even from the class itself and not of an instance of it.

```py
class Sample:
  number : int | float = 123

>>> Sample.number
123
```

Instance variables are attached to instances of the class only. They are not declared / defined unless called from a class instance.

```py
class Sample:
  def __init__(self) -> None:
    self.number : int | float = 123

>>> Sample.number
AttributeError: type object 'Sample' has no attribute 'number'

>>> Sample().number
123
```

Moreover, class variables can be modified further by the instance variables as well. This way, a variable can be accessed with a default value and further updated when an instance is created.

```py
class Sample:
  number : int | float = None

  def __init__(self) -> None:
    self.number : int | float = 123

>>> Sample.number
None

>>> Sample().number
123
```

## Dunder Methods
Double underscore ( or dunder ) methods, also called Magic Methods, are methods that allow instances of a class to interact with the built-in functions and operators. Common example of this is the ` __init__ ` dunder method, which allows the passing of parameters for a certain instance of the class.

### ` __abs__(self) `
Called when the built-in ` abs() ` function is applied to an instance of the class.

**Example**
```py
class Sample:
  def __init__(self, number : int | float) -> None:
    self.number : int | float = number

  def __abs__(self) -> int | float:
    return abs(self.number)

sample = Sample(-123)

>>> abs(sample)
123
```

### ` __add__(self, other : Any) ` 
Returns a new third object from the addition of 2 other objects with the addition arithmetic operator.

**Parameters**:
- **other** : Any = 2nd operand to append

**Example**
```py
class Sample:
  def __init__(self, text : str) -> None:
    self.text : str = text

  def __add__(self, other : str) -> str:
    return self.text + other

sample = Sample("hello")

>>> sample + " world"
"hello world"
```

### ` __and__(self, other : Any) `
Implement the built-in ` & ` bitwise operator.

**Parameters**:
- **other** : Any = 2nd operand to contrast

**Example**
```py
class Sample:
  def __init__(self, number : int) -> None:
    self.number : int = number

  def __and__(self, other : int) -> int:
    return self.number & other

sample = Sample(10)

>>> sample & 8
8
```

**Explanation**
In binary, integer ` 10 ` is ` 00001010 `, and integer ` 8 ` is ` 00001000 `. With every bit aligned together, the ` & ` bitwise operator drops a ` 1 ` if the corresponding aligned bits are both ` 1 `, otherwise ` 0 `.

```
  00001001 = 10
& 00001000 = 8
----------
  00001000 = 8
```

### ` __bool__(self) `
Implements the built-in ` bool() ` function.

**Example**
```py
class Sample:
  def __bool__(self) -> bool:
    return True

sample = Sample()

>>> bool(sample)
True
```

### ` __bytes__(self) `
Implement the built-in ` bytes() ` function.

**Example**
```py
class Sample:
  def __bytes__(self) -> bytes:
    return bytes(4)

>>> bytes(Sample())
b'\x00\x00\x00\x00'
```

### ` __call__(self, *args, **kwargs) `
Called when an instance of the class is called like a function.

**Parameters**:
- **args** : Optional = positional arguments
- **kwargs** : Optional = keyword arguments

**Example**
```py
class Sample:
  def __init__(self, text : str) -> None:
    self.text : str = text

  def __call__(self) -> str:
    return self.text

sample = Sample("hello world")

>>> sample()
"hello world"
```

### ` __ceil__(self) `
Implements the behavior of the ` math.ceil() ` function

**Example**
```py
from math import ceil

class Sample:
  def __init__(self, number : int | float) -> None:
    self.number : int | float = number

  def __ceil__(self) -> int:
    value : int = int(self.number)
    if value < self.number: value += 1
    return value

>>> ceil(Sample(12.34))
13
```

### ` __complex__(self) `
Implements the built-in ` complex() ` function

**Example**
```py
class Sample:
  def __complex__(self) -> complex:
    return 3 + 1j

>>> complex(Sample())
(3+1j)
```

> **NOTE**
> In Python, a complex number is represented as a pair of real numbers, where the first part is the real part and the second part is the imaginary part, followed by 'j' or 'J'.

### ` __contains__(self, value : Any) `
Called with the ` in ` keyword.

**Parameters**:
- **value** : Any = the value to look for

**Example**
```py
class Sample:
  def __init__(self, values : List[int]) -> None:
    self.values : List[int] = values

  def __contains__(self, value : int) -> bool:
    return value in self.values

>>> 2 in Sample([1, 2, 3])
True
```

### ` __del__(self) `
Called when an object or class instance is garbage collected or deleted.

**Example**
```py
class Sample:
  def __del__(self) -> None:
    print("Sample class instance is deleted")

>>> del Sample()
"Sample class instance is deleted"
```

### ` __delattr__(self, name : str) `
Called when there is an attempt of deleting an attribute.

**Parameters**:
- **name** : ` str ` = name of the attribute to delete

**Example**
```py
class Sample:
  def __setattr__(self, name : str, value : int) -> None:
    self.__dict__[name] = value

  def __delattr__(self, name : str) -> None:
    del self.__dict__[name]
    print(f"{name} attribute deleted")

sample = Sample()
sample.number : int = 123

>>> sample.number
123

>>> del sample.number
"number attribute deleted"
```

### ` __delitem__(self, index : Any) `
Called when the indexer operation is prefixed with the ` del ` keyword.

**Parameters**:
- **index** : Any = the index value to delete from the array

**Example**
```py
class Sample:
  values : List[int] = [1, 2, 3]

  def __delitem__(self, index : int) -> None:
    print(f"deleted value '{self.values[index]}' from the list")
    del self.values[index]

>>> del Sample()[2]
"deleted value '3' from the list"
```

### ` __dir__(self) `
Implements the built-in ` dir() ` function.

**Example**
```py
class Sample:
  numbers : List[int] = [1, 2, 3]

  def __dir__(self) -> List[int]:
    return self.numbers

>>> dir(Sample())
[1, 2, 3]
```

### ` __div__(self, other : Any) `
Implements the ` / ` floating-point division operation

**Parameters**:
- **other** : Any = 2nd operand

**Example**
```py
class Sample:
  number : int | float = 20

  def __div__(self, other : int) -> int | float:
    return self.number / other

>>> Sample() / 5
4
```

### ` __divmod__(self, other : Any) `
Implements the built-in ` divmod() ` method

**Parameters**:
- **other** : Any = 2nd operand

**Example**
```py
class Sample:
  number : int | float = 20

  def __divmod__(self, other : int | float) -> Tuple[int, int]:
    return divmod(self.number, other)

>>> divmod(Sample(), 6)
(3, 2)
```

### ` __enter__(self) `
Returns a value iven to the ` as ` keyword when used in a context manager with the ` with ` keyword

**Example**
```py
class Sample:
  def __enter__(self) -> str:
    return "hello world"

>>> with Sample() as sample:
...   print(sample)
"hello world"
```

### ` __eq__(self, other : Any) `
Customzies the behavior of the ` == ` equality operator

**Parameters**:
- **other** : Any = value to compare

**Example**
```py
class Sample:
  number : int | float = 2

  def __eq__(self, other : int) -> bool:
    return self.number == other

>>> Sample() == 2
True
```

### ` __exit__(self, exc_type : type, exc_value : Exception, exc_traceback : TracebackException) `
Called when the context manager is done processing.

**Parameters**:
- **exc_type** : ` type ` = class of the exception
- **exc_value** : ` Exception ` = type of the exception, such as ` DivisionByZero ` or ` FloatingPointError `
- **exc_traceback** : ` TracebackException ` = traceback object that has all the information needed to solve the exception

**Example**
```py
class Sample:
  def __enter__(self) -> None:
    print("entered context manager")

  def __exit__(self, exc_type : type, exc_value : Exception, exc_traceback : TracebackException) -> None:
    print("exited context manager")

>>> with Sample() as sample:
...   print("hello world")
"entered context manager"
"hello world"
"exited context manager"
```

### ` __float__(self) `
Implements the built-in ` float() ` function

**Example**
```py
class Sample:
  def __float__(self) -> float:
    return 42.3

>>> float(Sample())
42.3
```

### ` __floor__(self) `
Implements the behavior of the ` math.floor() ` function

**Example**
```py
from math import floor

class Sample:
  number : int | float = 14.56

  def __floor__(self) -> int:
    return int(self.number)

>>> floor(Sample())
14
```

### ` __floordiv__(self, other : Any) `
Implements the ` // ` integer division arithmetic operation

**Parameters**:
- **other** : Any = 2nd operand

**Example**
```py
class Sample:
  number : int | float = 7

  def __floordiv__(self, other : int) -> int:
    return self.number // other

>>> Sample() // 3
2
```

### ` __format__(self, specifier : Any) `
Implements the built-in ` format() ` function

**Parameters**:
- **specifier** : Any = format specifier value

**Example**
```py
class Sample:
  def __format__(self, specifier : str) -? str:
    return f"hello {specifier}"

>>> format(Sample(), "world")
"hello world"
```

### ` __ge__(self, other : Any) `
Customize the behavior of the ` >= ` greater-than-or-equal-to operator

**Parameters**:
- **other** : Any = 2nd operand

**Example**
```py
class Sample:
  number : int | float = 5

  def __ge__(self, other : int | float) -> bool:
    return self.number >= other

>>> Sample() >= 3
True
```

### ` __getattr__(self, attribute : str) `
Called when it failed to access an attribute

**Parameters**:
- **attribute** : ` str ` = name of the attribute that was attempted to retrieve

**Example**
```py
class Sample:
  number : int | float = 123

  def __getattribute__(self, attribute : str) -> Any:
    return super().__getattribute__(attribute)

  def __getattr__(self, attribute : str) -> None:
    print(f"Attribute {attribute} was not found")

>>> Sample().number
123

>>> Sample().name
"Attribute name was not found"
```

### ` __getattribute__(self, attribute : str) `
Called when trying to access an attribute

**Parameters**:
- **attribute** : ` str ` = name of the attribute to access

**Example**
```py
class Sample:
  number : int | float = 123

  def __getattribute__(self, attribute : str) -> Any:
    return super().__getattribute__(attribute)

>>> Sample().number
123
```

### ` __getitem__(self, index : Any) `
Called with the ` [] ` indexer operation

**Parameters**:
- **index** : Any = the index of the value to retrieve

**Example**
```py
class Sample:
  numbers : List[int] = [1, 2, 3]

  def __getitem__(self, index : int) -> int:
    return self.numbers[index]

>>> Sample()[1]
2
```

### ` __gt__(self, other : Any) `
Customize the behavior of the ` > ` greater-than inequality operator

**Parameters**:
- **other** : Any = 2nd operand

**Example**
```py
class Sample:
  number : int | float = 5

  def __gt__(self, other : int) -> bool:
    return self.number > other

>>> Sample() > 3
True
```

### ` __hash__(self) `
Implements the built-in ` hash() ` function

**Example**
```py
class Sample:
  def __hash__(self) -> int:
    return 43

>>> hash(Sample())
43
```

### ` __init__(self, *args, **kwargs) `
Called when an instance of the class is initialized

**Parameters**:
- **args** : Optional = positional arguments
- **kwargs** : Optional = keyword arguments

**Example**
```py
class Sample:
  def __init__(self, number : int | float) -> None:
    self.number : int | float = number

>>> sample = Sample(123)
>>> sample.number
123
```

### ` __int__(self) `
Implements the built-in ` int() ` function

**Example**
```py
class Sample:
  def __int__(self) -> int:
    return 43

>>> int(Sample())
43
```

### ` __invert__(self) `
Implements the behavior of the ` ~ ` bitwise NOT operator

**Example**
```py
class Sample:
  number : int | float = 13
  
  def __invert__(self) -> int:
    return ~self.number

>>> ~Sample
-14
```

**Explanation**
Integers are turned into binary and added ` 1 ` to it before negated.
```
   1101 |  13
+  0001 |   1
------- | ---
~  1110 |  14
------- | ---
  -1110 | -14
```

### ` __iter__(self) `
Called with the built-in ` iter() ` function or in a ` for ` loop

**Example**
```py
class Sample:
  values : List[int] = [1, 2, 3]

  def __iter__(self) -> Iterable:
    return self.values

>>> iter(Sample())
[1, 2, 3]
```

### ` __le__(self, other : Any) `
Customize the behavior of the ` <= ` less-than-or-equal-to inequality operator

**Parameters**:
- **other** : Any = 2nd operand

**Example**
```py
class Sample:
  number : int = 5

  def __le__(self, other : int) -> bool:
    return self.number <= other

>>> Sample() <= 3
False
```

### ` __len__(self) `
Implements the built-in ` len() ` function

**Example**
```py
class Sample:
  def __len__(self) -> int:
    return 123

>>> len(Sample())
123
```

### ` __lshift__(self, other : int) `
Implements the built-in ` << ` bitwise operation

**Parameters**:
- **other** : ` int ` = amount of bits to shift to the left

**Example**
```py
class Sample:
  number : int = 5

  def __lshift__(self, other : int) -> int:
    return self.number << other

>>> Sample() << 3
40
```

**Explanation**
The integer is converted into binary and is shifted to the left by ` n ` zeroes, where ` n ` is denoted by the ` other ` parameter -- when left-shifting, ` n ` zeroes are added from the right.

```
   0000 0101 |  5
<<       000 |  3
------------ | --
   0010 1000 | 40
```

### ` __lt__(self, other : Any) `
Implements the functionality of the ` < ` less-than inequality operator

**Parameters**:
- **other** : Any = 2nd operand

**Example**
```py
class Sample:
  number : int = 5

  def __lt__(self, other : int) -> bool:
    return self.number < other

>>> Sample() < 3
False
```

### ` __missing__(self, key : Any) `
Called when a non-existent key was attempted to access

**Parameters**:
- **key** : Any = the attempted non-existent key

**Example**
```py
class Sample:
  items : Dict[str, int] = {
    "a" : 1,
    "b" : 2,
    "c" : 3
  }

  def __missing__(self, key : str) -> None:
    print(f"Key {key} was not found in the items")

>>> Sample().items["d"]
"Key d was not found in the items"
```

### ` __mod__(self, other : Any) `
Implements the ` % ` modulo operation

**Parameters**:
- **other** : Any = 2nd operand

**Example**
```py
class Sample:
  number : int = 5

  def __mod__(self, other : int) -> int:
    return self.number % other

>>> Sample() % 2
1
```

### ` __mul__(self, other : Any) `
Implements the ` * ` arithmetic multiplication operation

**Parameters**:
- **other** : Any = 2nd operand

**Example**
```py
class Sample:
  number : int = 5

  def __mul__(self, other : int | float) -> int | float:
    return self.number * other

>>> Sample() * 2
10
```

### ` __ne__(self, other : Any) `
Customize the behavior of the ` != ` not-equal inequality behavior

**Parameters**:
- **other** : Any = 2nd operand

**Example**
```py
class Sample:
  number : int = 5

  def __ne__(self, other : int | float) -> bool:
    return self.number != other

>>> Sample() != 3
True
```

### ` __neg__(self) `
Implements the ` - ` negation operator

**Example**
```py
class Sample:
  number : int = 5

  def __neg__(self) -> int:
    return -self.number

>>> -Sample()
-5
```

### ` __new__(cls, *args, **kwargs) `
A static method that takes the class as its first argument and returns a new instance of that class

**Parameters**:
- **cls** : ` type ` = a class to create a new instance of
- **args** : Optional = positional arguments
- **kwargs** : Optional = keyword arguments

**Example**
```py
class Sample:
  def __new__(cls, *args, **kwargs) -> Self:
    print("Creating new instance")
    return super(Sample, cls).__new__(cls, *args, **kwargs)

  def __init__(self) -> None:
    print("__init__ called")

>>> Sample()
"Creating new instance"
"__init__ called"
```

> **NOTE**
> ` __new__ ` is called first before ` __init__ `.

### ` __next__(self) `
Called with the built-in ` next() ` function

**Example**
```py
class Sample:
  values : List[int] = [1, 2, 3]
  current : int = 0

  def __next__(self) -> int:
    self.current += 1
    return self.values[self.current]

>>> next(Sample())
2
```

### ` __or__(self, other : Any) `
Implements the built-in ` | ` bitwise OR operation

**Parameters**:
- **other** : Any = 2nd operand

**Example**
```py
class Sample:
  number : int = 13

  def __or__(self, other : int) -> int:
    return self.number | other

>>> Sample() | 7
15
```

**Explanation**
Integers are converted into binaries and aligned its bits correspondingly. The ` | ` bitwise OR operation drops ` 1 ` if any of the corresponding bit is ` 1 `, otherwise ` 0 `
```
  1101 | 13
| 0111 |  7
------ | --
  1111 | 15
```


### ` __pos__(self) `
Called to implement the ` + ` unary arithmetic operation

**Example**
```py
class Sample:
  number : int = -123

  def __pos__(self) -> int:
    return +self.number

>>> +Sample()
123
```


### ` __pow__(self, other : Any) `
Impements the built-in ` ** ` exponentiation operation

**Parameters**:
- **other** : Any = 2nd operand

**Example**
```py
class Sample:
  number : int = 5

  def __pow__(self, other : int) -> int:
    return self.number ** other

>>> Sample() ** 2
25
```


### ` __repr__(self) `
Implements the built-in ` repr() ` function. It returns a more information-rich, or official, string representation of an object.

**Example**
```py
class Sample:
  number : int = 5

  def __repr__(self) -> str:
    return f"Sample(number = {self.number})"

>>> repr(Sample())
"Sample(number = 5)"
```


### ` __reversed__(self) `
Called with the built-in ` reversed() ` function

**Example**
```py
class Sample:
  numbers : List[int] = [1, 2, 3]

  def __reversed__(self) -> List[int]:
    return self.numbers[::-1]

>>> reversed(Sample())
[3, 2, 1]
```


### ` __round__(self, ndigits : int = 0) `
Implements the built-in ` round() ` function

**Parameters**:
- **ndigits** : ` int ` = round the number to this given precision. Defaults to ` 0 `

**Example**
```py
class Sample:
  number : float = 12.3456

  def __round__(self, ndigits : int = 0) -> int | float:
    return round(self.number, ndigits = ndigits)

>>> round(Sample())
12

>>> round(Sample(), 2)
12.35

>>> round(Sample(), -1)
10
```


### ` __rshift__(self, other : int) `
Implements the built-in ` >> ` bitwise right shift operation

**Parameters**:
- **other** : ` int ` = amount of places to shift to the right

**Example**
```py
class Sample:
  number : int = 123

  def __rshift__(self, other : int) -> int:
    return self.number >> other

>>> Sample() >> 5
3
```

**Explanation**
Integers are converted into binaries. ` other ` determines how many places to shift to the right.
```
   0111 1011 | 123
>> 0000 0    |   5
------------ | ---
   0000 0011 |   3
```


### ` __setattr__(self, name : str, value : Any) `
Called when setting a value to an attribute

**Parameters**:
- **name** : ` str ` = name of the variable to set the value to
- **value** : Any = value of the attribute

**Example**
```py
class Sample:
  def __setattr__(self, name : str, value : Any) -> None:
    self.__dict__[name] : Any = value

>>> sample = Sample()
>>> sample.number : int = 123
>>> sample.number
123
```


### ` __setitem__(self, index : Any, value : Any) `
Called when setting a value to an array with the ` [] ` indexer operation

**Parameters**:
- **index** : Any = the index to set the value to
- **value** : Any = the value of the array's index

**Example**
```py
class Sample:
  numbers : List[int] = [1, 2, 3]

  def __setitem__(self, index : int, value : int) -> None:
    self.numbers[index] : int = value

>>> sample = Sample()
>>> sample[1] : int = 5
>>> sample.numbers
[1, 5, 3]
```


### ` __str__(self) `
Implements the built-in ` str() ` function. Returns a human.readable, or informal, string representation of an object

**Example**
```py
class Sample:
  def __str__(self) -> str:
    return "hello world"

>>> str(Sample())
"hello world"
```


### ` __sub__(self, other : Any) `
Implements the ` - ` arithmetic substraction operation.

**Parameters**:
- **other** : Any = 2nd operand

**Example**
```py
class Sample:
  number : int = 5

  def __sub__(self, other : int) -> int:
    return self.number - other

>>> Sample() - 3
2
```


### ` __truediv__(self, other : Any) `
Implements the ` / ` normal division operation

**Parameters**:
- **other** : Any = 2nd operand

**Example**
```py
class Sample:
  number : int = 7

  def __truediv__(self, other : int) -> int | float:
    return self.number / other

>>> Sample() / 3
2.0
```


### ` __trunc__(self) `
Implements the behavior of the ` math.trunc() ` function

**Example**
```py
from math import trunc

class Sample:
  def __trunc__(self) -> int:
    return 32

>>> trunc(Sample())
32
```


### ` __xor__(self, other : Any) `
Implement the built-in ` ^ ` bitwise XOR operation

**Parameters**:
- **other** : Any = 2nd operand

**Example**
```py
class Sample:
  number : int = 13

  def __xor__(self, other : int) -> int:
    return self.number ^ other

>>> Sample() ^ 5
8
```

**Explanation**
Integers are converted into binaries. Bitwise XOR operation returns ` 1 ` if any of the corresponding bits is ` 1 ` but not both, otherwise ` 0 `.
```
  1101 | 13
^ 0101 |  5
------ | --
  1000 |  8
```