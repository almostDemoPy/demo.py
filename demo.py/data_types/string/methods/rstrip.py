"""

str.rstrip(
  chars : Optional[str] = " "
)

- Return a copy of the string with trailing characters removed

================================================================

Parameters :

chars : Optional[str] = a string specifying the set of
    characters to be removed. Defaults to spaces

"""

string : str = "     sample string     "
print(string.rstrip())
# "     sample string"


string : str = "sample stringdnwaoidnawo"
print(string.rstrip("dnwaoi"))
# "sample string"