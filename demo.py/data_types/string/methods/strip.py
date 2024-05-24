"""

str.strip(
  chars : str
)

- Strip all both leading and trailing characters

===============================================================

Parameters :

chars : str = a string specifying the set of characters to be
    removed. Defaults to spaces

"""

string : str = "     sample string     "
print(string.strip())
# "sample string"


string : str = "ndowmpjfsample stringmdwpaodm"
print(string.strip("ndowmpjfa"))
# "sample string"