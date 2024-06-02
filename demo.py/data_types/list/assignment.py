"""

variable_name : list = [...]

- in replace of the ellipsis, any data type can be stored
    in the list

"""


sample_list : list = []
print(sample_list)
# []


# Case : contains data type of string

sample_list : list[str] = ["a", "b", "c"]
print(sample_list)
# ["a", "b", "c"]


# Case : contains data type of integers

sample_list : list[int] = [1, 2, 3]
print(sample_list)
# [1, 2, 3]


# Case : contains data type of floats

sample_list : list[float] = [1.0, 2.0, 3.0]
print(sample_list)
# [1.0, 2.0, 3.0]


# Case : contains lists, dictionaries, sets

sample_list : list[Union[list, dict, set]] = [
  [1, 2, 3],
  {
    "a": "A",
    "b": "B",
    "c": "C"
  },
  {1, 2, 3}
]


# Case : contians multiple data types

sample_list : list | list[Any] = ["a", 2, [3, 4], "five"]