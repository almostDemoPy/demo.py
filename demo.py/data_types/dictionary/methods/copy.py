"""

dictionary.copy()

- Returns a shallow copy of the dictionary

"""

dictionary_one : dict[int, int] = {
  1 : 2,
  3 : 4,
  5 : 6
}
dictionary_two : dict[int, int] = dictionary_one.copy()
print(dictionary_one)
# {1: 2, 3: 4, 5: 6}
print(dictionary_two)
# {1: 2, 3: 4, 5: 6}