# Mutable Objects
As oppose to immutable objects, mutables can be further modified after declaration. Such mutable objects are ` list `s, ` dict `s, and ` set `s.
```py
sample_list : List[int] = [1, 2, 3]
sample_dict: Dict[int, int] = {
  1 : 2,
  3 : 4,
  5 : 6
}
sample_set : Set[int] = {1, 2, 3}

>>> sample_list[0] = 0
>>> sample_list
[0, 2, 3]

>>> sample_dict[3] = 6
>>> sample_dict
{1: 2, 3: 6, 5: 6}

>>> sample_set.append(4)
>>> sample_set
{1, 2, 3, 4}
```