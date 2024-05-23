"""

str.maketrans(
  replaced : str,
  replacements : str,
  deleted : Optional[str]
)

- Construct a transition table [ of list of characters ] that
    need to be replaced or deleted from the string

===============================================================

Parameters :

replaced : str = list of character that need to be replaced

replacements : str = list of characters with which the
    characters need to be replaced

deleted : Optional[str] = list of characters that needs to be
    deleted

"""

string : str = "dimple- strong"
replaced : str = "dio"
replacements : str = "sai"
deleted : str = "-"
table : dict[int, int | None] = string.maketrans(replaced, replacements, deleted)
print(table)