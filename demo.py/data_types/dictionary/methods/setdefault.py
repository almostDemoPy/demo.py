"""

dictionary.setdefault(
  key : Any,
  value : Optional[Any] = None
)

- Returns the value of a key if the key is in the dictionary.
    Otherwise it inserts a key with the value to the dictionary

===============================================================

Parameters :

key : Any = key to be searched

value : Optional[Any] = key-value pair to be inserted in the
    dictionary if the key is not present in the dictionary.
    Defaults to None

"""

dictionary : dict[int, int] = {
  1 : 2,
  3 : 4,
  5 : 6
}
element : int = dictionary.setdefault(3)
print(element)
# 4
print(dictionary)
# {1: 2, 3: 4, 5: 6}


# Case : key does not exist

dictionary : dict[int, int] = {
  1 : 2,
  3 : 4,
  5 : 6
}
element : None = dictionary.setdefault(7)
print(element)
# None
print(dictionary)
# {1: 2, 3: 4, 5: 6, 7: None}


# Case : key does not exist and a default value is provided

dictionary : dict[int, int] = {
  1 : 2,
  3 : 4,
  5 : 6
}
element : int = dictionary.setdefault(7, 8)
print(element)
# 8
print(dictionary)
# {1: 2, 3: 4, 5: 6, 7: 8}