"""

str.translate(
  table : dict,
  deleted : Optional[str]
)

- Translate the characters using a translation table

===============================================================

Parameters :

table : dict = the translation table

deleted : Optional[str] = the string to be deleted or removed

"""

string : str = "dimple- strong"
replaced : str = "dio"
replacements : str = "sai"
deleted : str = "-"
table : dict[int, int | None] = string.maketrans(replaced, replacements, deleted)
print(string.translate(table))
# sample string


# Case : translate without using maketrans()

string : str = "dimple- strong"
table : dict[int, int | None] = {100 : 115, 105 : 97, 111 : 105, 45 : None} # ASCII
print(string.translate(table))
# sample string