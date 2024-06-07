"""

dictionary.pop(
  key : Any,
  value : Optional[Any]
)

- Remove and return the specified element

===============================================================

Parameters :

key : Any = the key whose key-value pair hsa to be returned
    and removed

value : Optional[Any] = default value to return if specified
    key is not present

===============================================================

Exceptions :

KeyError = key is not present and default value is not
    specified

"""

dictionary : dict[int, int] = {
  1 : 2,
  3 : 4,
  5 : 6
}
element : int = dictionary.pop(3)
print(element)
# 4
print(dictionary)
# {1: 2, 5: 6}


# Case : key does not exist

dictionary : dict[int, int] = {
  1 : 2,
  3 : 4,
  5 : 6
}
element : int = dictionary.pop(6)
# KeyError: 6


# Case : key does not exist and default value is provided

dictionary : dict[int, int] = {
  1 : 2,
  3 : 4,
  5 : 6
}
element : int = dictionary.pop(6, 7)
print(element)
# 7
print(dictionary)
# {1: 2, 3: 4, 5: 6}