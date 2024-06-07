"""

dictionary.popitem()

- Removes the last inserted key-value pair from the dictionary
    and returns it as a tuple

"""

dictionary : dict[int, int] = {
  1 : 2,
  3 : 4,
  5 : 6
}
item : tuple[int] = dictionary.popitem()
print(item)
# (5, 6)