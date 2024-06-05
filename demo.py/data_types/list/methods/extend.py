"""

list.extend(
  iterable : Union[list, set, dict, tuple]
)

- Adds items of an iterable at the end of a list

===============================================================

Parameters :

iterable : Union[list, set, dict, tuple] = any iterable

"""

first_list : list[int] = []
second_list : list[int] = [1, 2, 3]
first_list.extend(second_list)
print(first_list)
# [1, 2, 3]


# Case : sets

sample_list : list[int] = [1, 2, 3]
sample_set : set[int] = {4, 5, 6}
sample_list.extend(sample_set)
print(sample_list)
# [1, 2, 3, 4, 5, 6]


# Case : dict

sample_list : list[int] = [1, 2, 3]
sample_dict : dict[str, int] = {
  "d": 4,
  "e": 5,
  "f": 6
}
sample_list.extend(sample_dict)
print(sample_list)
# [1, 2, 3, "d", "e", "f"]


# Case : tuple

sample_list : list[int] = [1, 2, 3]
sample_tuple : tuple[int] = (4, 5, 6)
sample_list.extend(sample_tuple)
print(sample_list)
# [1, 2, 3, 4, 5, 6]