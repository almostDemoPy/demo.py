# Dictionary
Dictionaries are hashmaps. They store key-value pairs. Dictionary keys can be a string, integer, function, boolean, float, or an object.

A dictionary is denoted by enclosing ` {} ` curly braces. Its key-value pairs are separated by a ` , ` command, and a ` : ` colon is used to denote a key ( left-hand side ) and a value ( right-hand side ).
```py
sample : Dict[str, int] = {
  "a" : 1,
  "b" : 2,
  "c" : 3
}
```

## Dictionary Comprehensions
Dictionary Comprehensions are builder notations that helps make the setting up of the dictionary faster. Dictionary comprehensions are declared with the following syntax:
```py
{<action | key:value> <iteration statement> <Optional: conditional statement>}
```

**Example**
```py
characters : List[str] = ["a", "b", "c"]
numbers : List[int] = [1, 2, 3]
sample : Dict[str, int] = {
  character : number
  for _, (character, number) in enumerate(zip(characters, numbers))
}
```


## Dictionary Methods


### ` clear() `
Remove all items from the dictionary

**Example**
```py
sample : Dict[int, int] = {
  1 : 2,
  3 : 4,
  5 : 6
}

>>> sample.clear()
>>> sample
{}
```


### ` copy() `
Returns a shallow copy of the dictionary

**Example**
```py
sample : Dict[int, int] = {
  1 : 2,
  3 : 4,
  5 : 6
}

>>> sample_copy : Dict[int, int] = sample.copy()
>>> sample_copy
{1: 2, 3: 4, 5: 6}
```


### *classmethod* ` fromkeys(sequence : Sequence, value : Optional[Any]) `
Creates a new dictionary from the given sequence with the given default value, if specified.

**Parameters**:
- **sequence** : Sequence = a sequence of items containing the keys for the dictionary
- **value** : Optional[Any] = inital values for the generated keys. Defaults to ` None `

**Example**
```py
sequence : List[int] = [1, 2, 3]
sample : Dict[int, None] = dict.fromkeys(sequence)

>>> sample
{1: None, 2: None, 3: None}
```


### ` get(key : Any, value : Optional[Any]) `
Returns the value for the given key in the dictionary, otherwise returns the ` value ` if not found.

**Parameters**:
- **key** : Any = the key to look for
- **value** : Any = return value if ` key ` is not found in the dictionary. Defaults to ` None `

**Example**
```py
sample : Dict[str, int] = {
  "a" : 1,
  "b" : 2,
  "c" : 3
}

>>> sample.get("b")
2

>>> sample.get("d")
None

>>> sample.get("d", 4)
4
```


### ` items() `
Returns a list with all the keys and its corresponding values

**Example**
```py
sample : Dict[str, int] = {
  "a" : 1,
  "b" : 2,
  "c" : 3
}

>>> sample.items()
[("a", 1), ("b", 2), ("c", 3)]
```


### ` keys() `
Returns a view object that displays a list of all the keys in the dictionary

**Example**
```py
sample : Dict[str, int] = {
  "a" : 1,
  "b" : 2,
  "c" : 3
}

>>> sample.keys()
dict_keys(["a", "b", "c"])
```


### ` pop(key : Any, value : Optional[Any]) `
Removes and returns the specified element from the key

**Parameters**:
- **key** : Any = key whose key-value pair is to be removed and its value is returned
- **value** : Optional[Any] = default return value if specified key is not present in the dictionary

**Example**
```py
sample : Dict[str, int] = {
  "a" : 1,
  "b" : 2,
  "c" : 3
}

>>> sample.pop("b")
2

>>> sample
{"a": 1, "c": 3}

>>> sample.pop("d", 4)
4
```


### ` popitem() `
Removes the last inserted key-value pair and returns it as a ` tuple `

**Example**
```py
sample : Dict[str, int] = {
  "a" : 1,
  "b" : 2,
  "c" : 3
}

>>> sample.popitem()
("c", 3)
```


### ` setdefault(key : Any, value : Optional[Any]) `
Returns the value of a key if present in the dictionary, otherwise it inserts a key with the specified value

**Parameters**:
- **key** : Any = key to be searched
- **value** : Optional[Any] = default value of the key-value pair if ` key ` is not present in the dictionary. Defaults to ` None `

**Example**
```py
sample : Dict[str, int] = {
  "a" : 1,
  "b" : 2,
  "c" : 3
}

>>> sample.setdefault("c")
3

>>> sample.setdefault("d")
None

>>> sample
{"a": 1, "b": 2, "c": 3, "d": None}
```


### ` update(items : Union[Dict, Iterable]) `
Update the dictionary with the elements from another dictionary object or from an iterable of key-value pairs

**Parameters**:
- **items** : Union[Dict, Iterable] = another dictionary or iterable of key-value pairs to update to the dictionary

**Example**
```py
sample : Dict[str, int] = {
  "a" : 1,
  "b" : 2,
  "c" : 3
}

>>> sample.update({"c" : 4, "d" : 5})
>>> sample
{"a": 1, "b": 2, "c": 4, "d": 5}

>>> sample.update(c = 3, d = 4)
>>> sample
{"a": 1, "b": 2, "c": 3, "d": 4}

>>> sample.update([("e", 5)])
>>> sample
{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
```


### ` values() `
Returns a view object of a list containing the values in the dictionary

**Example**
```py
sample : Dict[str, int] = {
  "a" : 1,
  "b" : 2,
  "c" : 3
}

>>> sample.values()
dict_values([1, 2, 3])
```