# List
Lists are arrays or containers that stores values inside called **items**, often called **elements**. These itmes can be of any type, let it be a string, integer or float, dictionary or tuple, an object or a function, or another list ( which results in a nested list ).

Declaration of lists are denoted by enclosing ` [] ` square brackets.
```py
sample : List = []

>>> sample
[]

>>> type(sample)
<class 'list'>
```


## List Comprehensions
List comprehensions allows you to create a list easily with just 1 line. The syntax for a list comprehension is as follows:
```py
[<action> <iteration statement> <Optional: conditional statement>]
```

**Example**
```py
sample : List[int] = [i for i in range(5)]

>>> sample
[0, 1, 2, 3, 4]
```


## List Indexing
Indexing on a list returns a single element or item, and is denoted by enclosing ` [] ` square brackets next to a list or variable. List Indexing starts at ` 0 ` and ends at ` n - 1 `, where ` n ` is the count of all items in the list. Indexes can also be negative, which starts at ` -1 `, refering to the last item in the list, and ` -n ` which is the first item of the list, where ` n ` is the count of all items in the list.

**Example**
```py
sample : List[int] = [1, 2, 3]

>>> sample[0]
1

>>> sample[2]
3

>>> sample[-1]
3
```


## List Slicing
Slicing a list returns a new list of values from the slice. These values are children of the list, and may be modified in some way. The syntax for slicing is as follows:
```
[start : end : step]
```
where ` start ` is the start of the slice and starts at ` 0 ` ( defaults to ` 0 ` ), ` end ` is the end of the slice and starts at ` 1 ` ( defaults to ` n - 1 ` ), and ` step ` determines the interval of items to take ( defaults to ` 1 ` ).

**Example**
```py
sample : List[int] = [1, 2, 3, 4, 5]

>>> sample[2:]
[3, 4, 5]

>>> sample[1:4]
[2, 3, 4]

>>> sample[::2]
[1, 3, 5]
```


## List Methods


### ` append(item : Any) `
Add items at the end of the list

**Parameters**:
- **item** : Any = the item or element to add

**Example**:
```py
sample : List[int] = []

>>> sample.append(1)
>>> sample
[1]

>>> sample.append(2)
>>> sample
[1, 2]
```


### ` clear() `
Removes all items from the list

**Example**
```py
sample : List[int] = [1, 2, 3]

>>> sample.clear()
>>> sample
[]
```


### ` copy() `
Returns a shallow copy of the list

**Example**
```py
sample : List[int] = [1, 2, 3]

>>> smaple_copy : List[int] = sample.copy()
>>> sample_copy
[1, 2, 3]
```


### ` count(item : Any) `
Returns the count of the occurences of an item in the list

**Parameters**:
- **item** : Any = the item to take count for

**Example**
```py
sample : List[int] = [1, 2, 3, 1, 3, 2, 3]

>>> sample.count(1)
2
```


### ` extend(iterable : Iterable) `
Add the items of an iterable at the end of a list

**Parameters**:
- **iterable** : Iterable = an iterable containing the items to append to the list

**Example**
```py
>>> [].extend([1, 2, 3])
[1, 2, 3]

>>> [].extend({1, 2, 3})
[1, 2, 3]

>>> [].extend({1: 2, 3: 4, 5: 6})
[1, 3, 5]

>>> [].extend((1, 2, 3))
[1, 2, 3]
```


### ` index(item : Any, start : Optional[int] = 0, end : Optional[int] = -1) `
Returns the index of the first occurence of the item in the list

**Parameters**:
- **item** : Any = the item to look for
- **start** : Optional[` int `] = starting index of the search. Defaults to ` 0 `
- **end** : Optional[` int `] = ending position of the search. Defaults to ` -1 `

**Example**
```py
sample : List[int] = [1, 3, 1, 3, 2, 1, 3]

>>> sample.index(3)
2

>>> sample.index(2)
4
```


### ` insert(index : int, item : Any) `
Insert an item at a specific index

**Parameters**:
- **index** : ` int ` = index at which the item is to be inserted
- **item** : Any = the item to insert

**Example**
```py
sample : List[int] = [1, 3]

>>> sample.insert(1, 2)
>>> sample
[1, 2, 3]

>>> sample.insert(0, 0)
>>> sample
[0, 1, 2, 3]
```


### ` pop(index : Optional[int] = -1 ) `
Removes an item at a specific index from the list

**Parameters**:
- **index** : Optional[` int `] = the index of the item to be removed and returned. Defaults to ` -1 ` or the last item in the list.

**Example**
```py
sample : List[int] = [1, 2, 3]

>>> sample.pop()
3

>>> sample.pop(0)
1

>>> sample
[2]
```


### ` remove(item : Any) `
Removes the first occurence of a given item from the list

**Parameters**:
- **item** : Any = the item to be removed

**Example**
```py
sample : List[int] = [1, 2, 3, 1, 2, 3]

>>> sample.remove(2)
>>> sample
[1, 3, 1, 2, 3]

>>> sample.remove(3)
>>> sample
[1, 1, 2, 3]
```


### ` reverse() `
Reverses all the items of the list in place

**Example**
```py
sample : List[int] = [1, 2, 3, 4, 5]

>>> smaple.reverse()
>>> sample
[5, 4, 3, 2, 1]
```


### ` sort(reverse : Optional[bool] = False, key : Optional[Callable] = None) `
Sorts the items of a list in ascending or descending order, and by the criteria of ` key ` if provided.

**Parameters**:
- **reverse** : Optional[` bool `] = whether to sort the items in ascending or descending order. Defaults to ` False `
- **key** : Optional[Callable] = A function to specify the specify the sorting criteria(s)

**Example**
```py
sample : List[int] = [1, 4, 2, 5, 7, 4, 2, 4, 6]

>>> sample.sort()
>>> sample
[1, 2, 2, 4, 4, 4, 5, 6, 7]

>>> def check(number : int) -> bool:
...   return number % 2 == 0
>>> sample.sort(reverse = False, key = check)
[1, 5, 7, 2, 2, 4, 4, 4, 6]
```

**Explanation**
Integer form of a boolan ` True ` and ` False ` are ` 1 ` and ` 0 ` respectively. ` False ` values come first and followed by ` True ` values in the ascending order, and vice versa in descending order. The ` check ` function returns ` True ` if the current ` number ` is divisible by ` 2 `, otherwise ` False `.