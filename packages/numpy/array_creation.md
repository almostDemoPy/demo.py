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