"""

dictionary.keys()

- Returns a view object that displays a list of all the keys
    in the dictionary

"""

dictionary : dict[int, int] = {
  1 : 2,
  3 : 4,
  5 : 6
}
print(dictionary.keys())
# dict_keys([1, 3, 5])