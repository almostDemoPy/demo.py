"""

variable : dict[Union[int, float, str, bool], Any] = {
  ... : ...,
  ...
}

"""

dictionary : dict[str, str] = {
  "a" : "A",
  "b" : "B",
  "c" : "C"
}
print(dictionary)
# {"a": "A", "b": "B", "c": "C"}


dictionary : dict[str, int] = {
  "a" : 1,
  "b" : 2,
  "c" : 3
}
print(dictionary)
# {"a": 1, "b": 2, "c": 3}


dictionary : dict[int, float] = {
  1 : 1.0,
  2 : 2.0,
  3 : 3.0
}
print(dictionary)
# {1: 1.0, 2: 2.0, 3: 3.0}


dictionary : dict[bool, int] = {
  True : 1,
  False : 0
}
print(dictionary)
# {True: 1, False: 0}