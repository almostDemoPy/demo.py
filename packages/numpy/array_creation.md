# Array Creation Routines

## From Shape or Value

### ` empty(shape, dtype = float, order = "C", *, device = None, like = None) `
Returns a new array with the given ` shape ` and ` dtype ` without any specified entries.

**Parameters**:
- **shape** : Union[Tuple[` int `], ` int `] = shape of the empty array
- **dtype** : Optional[` type `] = data type of the entries. Defaults to [` float64 `](https://numpy.org/doc/2.1/reference/arrays.scalars.html#numpy.float64)
- **order** : Literal[` "C" `, ` "F" `] = whether to store multi-dimensional data in row-major ( C-style ), or column-major ( Fortran-style ) order in memory. Defaults to ` C `
- **device** : Optional[` str `] = the device on which to place the created array. For Array-API interoperability only, so must be ` "cpu" ` if passed. Defaults to ` None `
- **like** : Optional[Array-like] = Reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as ` like ` supports the ` __array_function__ ` protocol, the result will be defined by it. In this case, it ensures the creation of an array object compatible with that passed in via this argument.

**Returns**: ` ndarray `

```py
from numpy import empty

>>> empty((2, 2))
array([[1.39210482148, 5.2834012040],
       [3.40285917057, 9.8490127501]])

>>> empty(2, dtype = int)
array([21419027401, 84012842190])
```

### ` empty_like(prototype, dtype = None, order = "K", subok = True, shape = None, * device = None) `
Return a new array with the same shape and type as the given ` prototype `

**Parameters**:
- **prototype** : Array-like = the shape and data type of ` prototype ` define the same attributes of the returned array
- **dtype** : Optional[` type `] = overrides the data type of the result
- **order** : Literal[` "C" `, ` "F" `, ` "A" `, ` "K" `] - overrids the memory layout of the result. ` "C" ` means C-order. ` "F" ` means F-order. ` "A" ` means ` "F" ` if ` prototype ` is Fortran contiguous, ` "C" ` otherwise. ` "K" ` means match the layout of ` prototype ` as closely as possible. Defaults to ` "K" `
- **subok** : ` bool ` = if ` True `, then the newly created array will use the sub-class type of ` prototype `, otherwise it will be a base-class array. Defaults to ` True `
- **shape** : Union[Sequence[` int `], ` int `] = overrides the shape of the result. If ` order = "K" ` and the number of dimensions is unchanged, will try to keep the order, otherwise, ` order = "C" ` is applied
- **device** : Optional[` str `] = device on which to place the created array. For Array-API interoperability only, so must be ` "cpu" ` if passed. Defaults to ` None `

**Returns**: ` ndarray `

```py
from numpy import empty_like

a : Tuple[List[int]] = ([1, 2, 3], [4, 5, 6])
b : Tuple[List[float]] = ([1.0, 2.0, 3.0])

>>> empty_like(a)
array([[54175984579, 49302480142, 32148914842],
       [84120481294, 48912401294, 99100482481]])

>>> empty_like(b)
array([1.2002049040, 12.0420490294, 5.9402940238])
```

### ` eye(N, M = None, k = 0, dtype = float, order = "C", *, device = None, like = None) `
Returns a 2D array with ` 1 `s  on the diagonal and ` 0 `s elswhere

**Parameters**:
- **N** : ` int ` = number of rows
- **M** : Optional[` int `] = number of columns. If ` None `, defaults to ` N `. Defaults to ` None `
- **k** : Optional[` int `] = index of the diagonal. ` 0 ` refers to the main diagonal. A positive value refers to an upper diagonal. A negative value refers to a lower diagonal. Defaults to ` 0 `
- **dtype** : Optional[` type `] = data type of the returned array. Defaults to ` float `
- **order** : Optional[Literal[` "C" `, ` "F" `]] - whether the output should be stored in row-major ( C-style ) or column-major ( Fortran-style ) order in memory
- **device** : Optional[` str `] = device on which to place the created array. For Array-API interoperability only, so must be ` "cpu" ` if passed. Defaults to ` None `
- **like** : Optional[` array-like `] = reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as ` like ` supports the ` __array_function__ ` protocol, the result will be defined by it. In this case, it ensures the creation of an array object compatible with that passed in via this argument.

**Returns**: ` ndarray `

```py
from numpy import eye

>>> eye(5, dtype = int)
array([[1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 0, 0, 1, 0],
       [0, 0, 0, 0, 1]])

>>> eye(5, dtype = int, k = 2)
array([[0, 0, 1, 0, 0],
       [0, 0, 0, 1, 0],
       [0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]])
```


### ` identity(n, dtype = float, *, like = None) `
Returns the identity array.

An identity array is a square array with ` 1 `s on the main diagonal.

**Parameters**:
- **n** : ` int ` = number of rows and columns
- **dtype** : Optional[` type `] = data type of the output
- **like** : Optional[` array-like `] = reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as ` like ` supports the ` __array_function__ ` protocol, the result will be defined by it. In this case, it ensures the creation of an array object compatible with that passed in via this argument.

**Returns**: ` ndarray `

```py
from numpy import identity

>>> identity(5)
array([[1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 0, 0, 1, 0],
       [0, 0, 0, 0, 1]])
```