"""

str.lstrip(
  characters : Optional[str] = " "
)

- Return a copy of the string with leading characters removed


Parameters :

characters : Optional[str] = Set of characters to remove as
    leading characters. Defaults to space.

"""

string : str = "   sample string   "
print(string.lstrip())
# "sample string   "


string : str = "abbcabacb sample string"
print(string.lstrip("abc"))
# "sample string"