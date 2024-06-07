"""

dict.fromkeys(
  sequence : Sequence,
  value : Optional[Any] = None
)

- Creates a new dictionary from the given sequence with the
    specific value.

===============================================================

Parameters :

sequence : Sequence = the sequence to be transformed into a
    dictionary

value : Optional[Any] = initial values that need to be assigned
    to the generated keys. Defaults to None

"""

sequence : tuple[int] = (1, 2, 3)
dictionary : dict[int, None] = dict.fromkeys(sequence)
print(dictionary)
# {1: None, 2: None, 3: None}


sequence : list[int] = [1, 2, 3]
dictionary : dict[int, str] = dict.fromkeys(sequence, "_")
print(dictionary)
# {1: "_", 2: "_", 3: "_"}