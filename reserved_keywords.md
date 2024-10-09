# Reserved Keywords
Reserved keywords are one of the basic syntaxes in Python. Naming your variables in any of these keyword names would not be possible.

## Keywords

### ` and `
Used to check if both operands are ` True `

**Syntax**
```py
x and y
```

**Example**
```py
>>> True and True
True

>>> True and False
False

>>> False and False
False
```


### ` as `
Aliases a returned object to a new identifier

**Syntax**
```py
# for imports:
import module as <variable>
from module import something as <variable>

# for context managers:
with something() as <variable>: ...
```

**Statements**:
- **variable** = the variable to store the returned value in

**Example**
```py
from datetime import datetime as dt

>>> dt.now()
'...'
```


### ` assert `
Usually used for debugging and checks.

**Syntax**
```py
assert <condition> [, on_false]
```

**Statements**:
- **condition** : ` bool ` = a condition statement indicating a code check
- **on_false** : Optional[Union[Callable, ` str `]] = what to say  when the ` condition ` statement returns ` False `. A function call may also be done in this statement.

**Raises**:
- **AssertionError** - the ` condition ` statement returned a ` False `-like value

**Example**
```py
sample : int = 5

def is_wrong() -> None:
  print("wrong")

>>> assert sample < 3
AssertionError

>>> assert sample < 3, "wrong"
AssertionError: wrong

>>> assert sample < 3, is_wrong()
"wrong"
AssertionError: None
```


### ` async `
Used to construct an asynchronous function or context manager. This is appended before the ` def ` or ` with ` keywords.

**Syntax**
```py
# for functions:
async def function() -> None: ...

# for context managers:
async with something() as x: ...
```

**Example**
```py
from asyncio import run

async def function() -> None:
  print("hello world")

>>> run(function())
"hello world"
```


### ` await `
Used to call an asynchronous function.

**Syntax**
```py
await function()
```

**Example**
```py
from asyncio import run

async def function() -> None:
  print("hello world")

async def main() -> None:
  await function()

>>> run(main())
"hello world"
```


### ` break `
Used to break out of the current loop. Applicable to ` for ` and ` while ` loops

**Syntax**
```py
break
```

**Example**
```py
def function() -> None:
  for i in range(5):
    print(i)
    if i % 2 == 1: break

>>> function()
0
1
```


### ` case `
Used inside ` match ` blocks, usually stores the expecting matching values for the variable in ` match ` statement

**Syntax**
```py
case <value>: ...
```

**Statements**:
- **value** : Any = expecting matching value for the variable in ` match ` statement. This can be an ` _ ` underscore, which accepts any value not matched from any previous ` case ` statements

**Example**
```py
sample : int = 4

>>> match sample:
...   case 1: print("first")
...   case 2: print("second")
...   case 3: print("third")
...   case _: print("something else")
"something else"
```


### ` class `
Used to construct a user-defined class

**Syntax**
```py
class <ClassName>[(subclasses, *args, **kwargs)]: ...
```

**Statements**:
- **ClassName** = name of the class. For conveniences and standards, classes are written in TitleCase
- **subclasses** : Optional[Any] = the classes to inherit for the constructing class
- **args** : Optional[Any] = positional arguments passed for subclassing
- **kwargs** : Optional[Any] = keyword arguments passed for subclassing

**Example**
```py
class Sample:
  string : str = "hello world"

>>> Sample.string
"hello world"
```


### ` continue `
Stops the current iteration and continues to the next iteration of the current loop

**Syntax**
```py
continue
```

**Example**
```py
def function() -> None:
  for i in range(5):
    if i == 3: continue
    print(i)

>>> function()
0
1
2
4
```


### ` def `
Used to define a function

**Syntax**
```py
def <function_name>([*args, **kwargs])[ -> <return_type>]: ...
```

**Statements**:
- **function_name** = name of the function
- **args** : Optional = positional arguments / parameters for the function
- **kwargs** : Optional = keyword arguments / parameters for the function
- **return_type** : Optional[` type `] = the type of what the function will return. Defaults to ` None `

**Example**
```py
def function() -> None:
  print("hello world")

>>> function()
"hello world"
```


### ` elif `
Shorthand for *else if*; checks if some other condition holds when the previous ` if ` or ` elif ` statement returned ` False `.

` elif ` statements are always sandwiched between ` if ` and ` else ` statements and is stackable, such that:
```py
if condition: ...
elif condition: ...
elif condition: ...
else: ...
```

**Syntax**
```py
elif <condition>: ...
```

**Statements**:
- **condition** : ` bool ` = condition to check

**Example**:
```py
sample : int = 5

>>> if sample < 5: print("less than")
... elif sample == 5: print("exact")
... else: print("greater than")
"exact"
```


### ` else `
Used to construct an ` else ` block. This block is executed only when the previous ` if ` and ` elif ` statements all returned a ` False `-like value. This can also be applie to the ` while ` block, and is executed when the ` condition ` statement for the loop is ` False `

**Syntax**
```py
# for if-elif-else block:
if condition: ...
elif condition: ...
else: ...

# for while loop:
while condition: ...
else: ...
```

**Example**
```py
sample : int = 1

>>> if sample > 3: print("greater than")
... elif sample == 3: print("exact")
... else: print("less than")
"less than"

>>> while sample < 3:
...   print(sample)
...   sample += 1
... else: print("loop ended")
1
2
"loop ended"
```


### ` except `
Catches the exception and constructs the error handling

**Syntax**
```py
try: ...
except [<exception> as [identifier]]: ...
```

**Statements**:
- **exception** : Optional[` Exception `] = the specific exception to catch. When specified as ` Exception `, all exception types are catched.
- **identifier** : Optional = the variable name for the catched exception

**Example**
```py
>>> try:
...   print(1 + "1")
... except TypeError as error:
...   print("cannot add an integer and a string")
"cannot add an integer and a string"
```


### ` False `
A boolean indicating a condition statement is not ` True `

**Syntax**
```py
False
```

**Example**
```py
>>> 1 == 2
False
```


### ` finally `
Always excutes after the ` try-except ` block regardless of the error, if any

**Syntax**
```py
try: ...
except: ...
finally: ...
```

**Example**
```py
>>> try:
...   raise Exception("an error occured")
... except Exception as error:
...   print("fixing errors")
... finally:
...   print("completing code")
"fixing errors"
"completing code"
```


### ` for `
Used to construct a ` for ` loop

**Syntax**
```py
for <declaration>: ...
```

**Statements**:
- **declaration** : Iterable = declaration of a variable from an iterable

**Example**
```py
>>> for i in range(4):
...   print(i)
0
1
2
3
```


### ` from `
Used to import a specific object from a module

**Syntax**
```py
from module import something
```

**Example**
```py
from math import pi

>>> pi
3.14...
```


### ` global `
Used to access and modify a variable in the global scope

**Syntax**
```py
global variable
```

**Example**
```py
x : int = 5

def function() -> None:
  global x
  x += 5
  print(x)

>>> function()
10
```


### ` if `
Used to construct an ` if ` statement

**Syntax**
```py
if <condition>: ...
```

**Statements**:
- **condition** : ` bool ` = the condition to check

**Example**
```py
sample : int = 5

>>> if sample == 5: print("exact")
"exact"
```


### ` import `
Used to import modules

**Syntax**
```py
import <module>
```

**Statements**:
- **module** = the module to import. This can be a local module ( python file ), an installed package / library, or of a built-in module by Python

**Example**
```py
import datetime

>>> datetime.datetime.now()
"..."
```


### ` in `
Used to check if an object is found in an array or sequence

**Syntax**
```py
<variable> in <array>
```

**Statements**:
- **variable** : Any = the variable to search for in the ` array `
- **array** : Any = a universal array to be searched for the ` variable `

**Example**
```py
numbers : List[int] = [1, 2, 3, 4, 5]

>>> 3 in numbers
True

>>> 6 in numbers
False
```


### ` is `
Used to check if the left operand references to an object ( right operand ) in memory

**Syntax**
```py
<variable> is <reference>
```

**Statements**:
- **variable** : Any = variable to check for
- **reference** : Any = the reference, typically a type, to check for the ` variable `

**Example**
```py
>>> 5 is 5.0
False

>>> 5 == 5.0
True
```


### ` lambda `
Used to create anonymous functions

**Syntax**
```py
lambda <args>: <statements>
```

**Statements**:
- **args** : Any = positional arguments / parameters to be passed to the lambda function
- **statements** = collection of statements by which the lambda function operates.

> **NOTE**
> Assignment operations do not work inside lambda functions, neither are multi-line codes.

**Example**
```py
sample : Callable[[int, int], int] = lambda x, y : return x + y

>>> sample(1, 2)
3
```


### ` match `
Used to construct ` match-case ` block

**Syntax**
```py
match <variable>
```

**Statements**:
- **variable** : Any = the [ value of a ] variable to match for

**Example**
```py
sample : bool = True

>>> match sample:
...   case False: print("is false")
...   case True: print("is true")
"is true"
```


### ` None `
Indicates a null value

**Syntax**
```py
None
```

**Example**
```py
sample : None = None

>>> sample is None
True
```


### ` nonlocal `
Used to reference a variable on the nearest scope.

**Syntax**
```py
nonlocal <variable>
```

**Statements**:
- **variable** = the variable to get the reference of

**Example**
```py
string : str = "hello"

def foo() -> str:
  string : str = "world"

  def bar() -> None:
    nonlocal string
    print(string)
    string = "python"

  bar()
  return string

>>> print(string)
"hello"

>>> foo()
"world"
"python"
```


### ` not `
Returns ` True ` when the value is ` False `, and vise versa

**Syntax**
```py
not <variable>
```

**Statements**:
- **variable** = variable to negate the value of

**Example**
```py
>>> not True
False

>>> not False
True
```


### ` or `
Returns ` True ` if either of the values are ` True `. When done in an assignment operation, the right operand is taken if the first operand is of ` False `-like value

**Syntax**
```py
x or y
```

**Example**
```py
>>> True or True
True

>>> True or False
True

>>> False or True
True

>>> False or False
False

>>> sample : str | None = None or "hello world"
>>> sample
"hello world"
```


### ` pass `
Used as a placeholder for future code

**Syntax**
```py
pass
```

**Example**
```py
class Sample: pass

def function() -> None: pass
```


### ` raise `
Used to raise an exception or error

**Syntax**
```py
raise <exception>
```

**Statements**:
- **exception** : ` Exception ` = the exception to raise

**Example**
```py
>>> raise Exception("something went wrong")
Exception: something went wrong
```


### ` return `
Used to exit a function and return a value

**Syntax**
```py
return <value> [, *values]
```

**Statements**
- **value(s)** : Any = the values to return to the originating call of the function, separated by ` , ` commas. Defaults to ` None `

**Example**
```py
def function() -> str:
  return "hello world"

>>> function()
"hello world"
```


### ` True `
Indicates a condition is ` True `

**Syntax**
```py
True
```

**Example**
```py
>>> 1 == 1
True

>>> True
True
```


### ` try `
Used to construct a ` try ` block

**Syntax**
```py
try: ...
```

**Example**
```py
>>> try:
...   print(1 + 2)
... except Exception as error:
...   print(error)
3
```


### ` type `
Used to construct a new type

**Syntax**
```py
type <name> = <annotations>
```

**Statements**:
- **name** = name of the type
- **annotations** = possible / expected annotations for the values with this corresponding type

**Example**
```py
type Number = int | float

sample : Number = 1.00

>>> sample
1.00

>>> type(sample)
<class 'float'>
```


### ` while `
Used to construct a ` while ` loop

**Syntax**
```py
while <condition>: ...
```

**Statements**:
- **condition** : ` bool ` = the condition to check in every iteration. When this becomes ` False `, the loop breaks

**Example**
```py
>>> sample : int = 1
>>> while sample < 3:
...   print(sample)
...   sample += 1
1
2
```


### ` with `
Used to construct a context manager

**Syntax**
```py
with <callable> as <identifier>: ...
```

**Statements**:
- **callable** : Callable = a callable that returns a value
- **identifier** = the identifier or the reference to the returned value of the ` callable `

**Example**
```py
>>> with open('file.txt', "r") as file:
...   lines = file.read()
>>> lines
"..."
```


### ` yield `
Used to create a generator function

**Syntax**
```py
yield <value>
```

**Statements**:
- **value** : Any = the value to return from the current iteration

**Example**
```py
from random import randint

def get_random(min : int, max : int, *, count : int = 1) -> int:
  for i in range(count):
    yield randint(min, max)

>>> for number in get_random(1, 3, count = 3):
...   print(number)
2
3
1
```