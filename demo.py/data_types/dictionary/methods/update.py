"""

dictionary.update(
  items : Union[dict, Iterable]
)

- Update the dictionary with the elements from another
    dictionary object or from an iterable of key-value pairs

===============================================================

Parameters :

items : Union[dict, Iterable] = the dictionary or iterable of
    key-value pairs to update to the dictionary

"""

dictionary : dict[int, int] = {}
new_data : dict[int, int] = {
  1 : 2
}
dictionary.update(new_data)
print(dictionary)
# {1: 2}


dictionary : dict[int, int] = {
  1 : 2,
  3 : 4,
  5 : 7
}
new_data : dict[int, int] = {
  5 : 6,
  7 : 8
}
dictionary.update(new_data)
print(dictionary)
# {1: 2, 3: 4, 5: 6, 7: 8}


# Case : update with iterable

dictionary : dict[int, int] = {}
dictionary.update(a = 1, b = 2)
print(dictionary)
# {"a": 1, "b": 2}


dictionary : dict[int, int] = {}
dictionary.update([(1, 2), (3, 4)])
print(dictionary)
# {1: 2, 3: 4}