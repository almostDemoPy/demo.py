# Type Annotations
Type annotations, sometimes called *type hinting*, lets the program and the developer know the type of the declared or returned variable. This is optional to do, but easier to understand what the code does or returns.

Annotations or type hinting are denoted by a ` : ` colon after the variable name, followed by the type.

**Syntax**
```py
sample : type = some_value
```


## Annotating Variables


### String Annotations
Annotations for strings are denoted by ` str `.

**Example**
```py
sample : str = "hello world"

>>> sample
"hello world"

>>> type(sample)
<class 'str'>
```


### Integer Annotations
Annotations for integers are denoted by ` int `.

**Example**
```py
sample : int = 123

>>> sample
123

>>> type(sample)
<class 'int'>
```


### Float Annotations
Annotations for floats are denoted by ` float `.

**Example**
```py
sample : float = 1.0

>>> sample
1.0

>>> type(sample)
<class 'float'>
```


### List Annotations
Annotations for lists can either be ` list `, or ` List ` from the ` typing ` module. It can be left ` List ` as is, or suffix it with enclosing ` [] ` square brackets and append union of annotations inside, noting the [ possible ] contents of the list.

**Example**
```py
sample : List[int] = [1, 2, 3]

>>> sample
[1, 2, 3]

>>> type(sample)
<class 'list'>
```


### Dictionary Annotations
Annotations for dictionaries can either be ` dict `, or ` Dict ` from the ` typing ` module. It can be left ` Dict ` as is, or suffix it with enclosing ` [] ` square brackets and append union of annotations inside, noting the [ possible ] contents of the dictionary. If done, it can take 2 parameters: annotation for the ` key ` values, and another [ union of ] annotations for the ` values ` of the ` key `s.

**Example**
```py
sample : Dict[str, int] = {
  "a" : 1,
  "b" : 2,
  "c" : 3
}

>>> sample
{"a": 1, "b": 2, "c": 3}

>>> type(sample)
<class 'dict'>
```


### Tuple Annotations
Annotations for tuples are denoted by ` tuple `, or ` Tuple ` from the ` typing ` module. It can be left ` Tuple ` as is, or suffix it with enclosing ` [] ` square brackets and append [ union of ] annotations insde, noting the [ possible ] contents of the tuple.

**Example**
```py
sample : Tuple[int] = 1, 2, 3

>>> sample
(1, 2, 3)

>>> type(sample)
<class 'tuple'>
```


### None Annotations
Annotations for nonetype variables / values are denoted by ` None `.

**Example**
```py
sample : None = None

>>> sample
None

>>> type(sample)
<class 'NoneType'>
```


### Class Annotations
Annotations for class instances are denoted by the class' name.

**Example**
```py
class Sample: ...

sample : Sample = Sample()

>>> type(sample)
<class 'Sample'>
```


## Union of Annotations
Annotations can be grouped in one placement / position. This can be done through the ` | ` bitwise-OR syntax, or ` Union ` annotation from the ` typing ` module. Appending the annotations as a union indicates that the type of the variables or values can or may be either of the specified.

**Example**
```py
sample : int | float = 1.0

>>> sample
1.0

>>> type(sample)
<class 'float'>
```

When using ` Union `, types inserted inside its ` [] ` square brackets do not need to be between ` | ` bitwise-OR anymore.

**Example**
```py
sample : Union[int, float] = 1.0

>>> sample
1.0

>>> type(sample)
<class 'float'>
```


## Return Annotations
Return values of functions can be annotated. By default, the function is annotated as ` None `.

Annotating the return value of a function is denoted by an ` -> ` arrow syntax, followed by the type annotation. This is done after the function definition, just before the ` : ` colon.

**Example**
```py
def sample() -> None:
  print("hello world")

>>> sample()
"hello world"

def sample() -> int:
  return 123

>>> sample()
123
```