"""

dictionary.values()

- Returns a view object containing the values of the dictionary

"""

dictionary : dict[int, int] = {
  1 : 2,
  3 : 4,
  5 : 6
}
print(dictionary.values())
# dict_values([2, 4, 6])