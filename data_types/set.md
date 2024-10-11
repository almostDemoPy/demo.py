# Set
Sets are containers whose elements are ordered and does not contain duplicates. Unlike dictionaries, sets do not store elements in a key-value pair behavior, but instead are in singulare element like in a list.

A set is declared with enclosing ` {} ` curly braces.
**Example**
```py
sample : Set[int] = {1, 2, 3}
```

A set can be declared with duplicate of elements in it, and can be in any order. Though this is modified by Python and later will be in ascending order and the duplicates are removed.
```py
sample : Set[int] = {1, 2, 5, 2, 1, 4}

>>> sample
{1, 2, 4, 5}
```


## Set Methods


### ` add(element : Any) `
Adds an element to the set if it is not present yet

**Parameters**:
- **element** : Any = the element to add

**Example**
```py
sample : Set[int] = {}

>>> sample.add(1)
>>> sample
{1}
```


### ` clear() `
Removes all elements from the set

**Example**
```py
sample : Set[int] = {1, 2, 3}

>>> sample.clear()
>>> sample
{}
```


### ` copy() `
Creates a shallow copy of the set

**Example**
```py
sample : Set[int] = {1, 2, 3}

>>> sample_copy : Set[int] = sample.copy()
>>> sample_copy
{1, 2, 3}
```


### ` difference_update(set : Set[int]) `
Returns the difference of 2 sets and updates the set with the difference

**Parameters**:
- **set** : Set[` int `] = set whose difference is to take from the first set

**Example**
```py
sample : Set[int] = {1, 2, 3}

>>> smaple.difference_update({2, 4, 6})
>>> sample
{1, 3}
```

**Explanation**
When subtracting 2 sets, the elements of the first set are removed if it's present in the second set. Since the element ` 2 ` is also present in the second set, it is removed from the first set.


### ` difference(set : Set) `
Returns the difference of the 2 sets

**Parameters**:
- **set** : Set = the 2nd set whose difference is to take from the first set

**Example**
```py
sample : Set[int] = {1, 2, 3}

>>> sample.difference({2, 4, 6})
{1, 3}
```

> **NOTE**
> 
> This does not update the first set. If you wish to update the first set with the difference of 2 sets, use ` difference_update() ` instead.


### ` discard(element : Any) `
Removes an element from the set

**Parameters**:
- **element** : Any = the element to be removed

**Example**
```py
sample : Set[int] = {1, 2, 3}

>>> sample.discard(2)
>>> sample
{1, 3}
```


### ` intersection_update(sets : Set, ...) `
Updates the first set with the common element of the provided sets

**Parameters**:
- **sets** : Set = the sets to get the common elements of the first set with

**Example**
```py
sample : Set[int] = {1, 2, 3}

>>> sample.intersection_update({2, 3, 4})
>>> sample
{2, 3}
```


### ` intersection(sets : Set, ...) `
Returns a new set with the common elements of the provided set with the first set

**Parameters**:
- **sets** : Set = sets to retrieve the common elements of with the first element

**Example**
```py
sample : Set[int] = {1, 2, 3}

>>> sample.intersection({2, 3, 4})
{2, 3}
```

> **NOTE**
> 
> This does not update the first set. If you wish to update the first set with the common elements of all provided sets with it, use ` intersection_update() ` instead.


### ` isdisjoint(set : Set) `
Check whether the two sets are disjoin.

The two sets are considered disjoint if there is no common elements between the two sets.

**Parameters**:
- **set** : Set = second set to compare with

**Example**
```py
sample : Set[int] = {1, 2, 3}

>>> sample.isdisjoint({4, 5, 6})
True

>>> sample.isdisjoint({2, 3, 4})
False
```


### ` issubset(set : Set) `
Check whether all elements in set B are present in set A

**Parameters**:
- **set** : Set = the subset to compare to the first set

**Example**
```py
sample : Set[int] = {1, 2, 3, 4, 5}

>>> {1, 3, 5}.issubset(sample)
True

>>> {2, 4, 6, 8}.issubset(sample)
False
```

> **NOTE**
> 
> An empty set ` {} ` is always a subset to any set.


### ` issuperset(set : Set) `
Check if all elements of set A are in set B

**Parameters**:
- **set** : Set = second set to compare with

**Example**
```py
sample : Set[int] = {1, 2, 3, 4, 5}

>>> sample.issuperset({1, 3, 5})
True

>>> sample.issuperset({6, 7})
False
```

> **NOTE**
> 
> An ` {} ` empty set is always a subset of any superset.


### ` pop() `
Removes and returns any random element from the set

**Example**
```py
sample : Set[int] = {1, 2, 3}

>>> sample.pop()
2

>>> sample
{1, 3}
```


### ` remove(element : Any) `
Remove an element from the set

**Parameters**:
- **element** : Any = the element to remove

**Example**
```py
sample : Set[int] = {1, 2, 3}

>>> sample.remove(2)
>>> sample
{1, 3}
```


### ` symmetric_difference_update(set : Set) `
Update the first set with the symmetric difference of the two sets

**Parameters**:
- **set** : Set = second set to compare with

**Example**
```py
sample : Set[int] = {1, 2, 3}

>>> sample.symmetric_difference_update({2, 3, 4})
>>> sample
{1, 4}
```

**Explanation**
The symmetric difference of two sets is a set whose elements are not found in both of the sets.


### ` symmetric_difference(set : Set) `
Return a new set with the symmetric difference of the two sets

**Parameters**:
- **set** : Set = second set to compare with

**Example**
```py
sample : Set[int] = {1, 2, 3}

>>> sample.symmetric_difference({2, 3, 4})
{1, 4}
```

**Explanation**
The symmetric difference of two sets is a set whose elements are not found in both of the sets.

> **NOTE**
> 
> This does not update the first set. If you wish to update the first set with the symmetric difference of the two sets, use ` symmetric_difference_update() ` instead.


### ` untion(set : Set, ...) `
Returns a new set that contains all the elements of all the provided set and the first set

**Parameters**:
- **set** : Set = sets to compare with

**Example**
```py
sample : Set[int] = {1, 2, 3}

>>> sample.union({2, 3, 4})
{1, 2, 3, 4}
```


### ` update(set : Set) `
Adds elements to the set

**Parameters**:
- **set** : Set = a set containing the elements to add to the first set

**Example**
```py
sample : Set[int] = {1, 2, 3}

>>> sample.update({3, 4, 5})
>>> sample
{1, 2, 3, 4, 5}
```