"""

str.rpartition(
  separator : str
)

- Split the string into three parts, starting from the right
    side : left-hand side of separator, separator, right-hand
    side of separator

===============================================================

Parameters :

separator : str = separates the string

===============================================================

Exceptions :

ValueError : empty separator

"""

string : str = "sample in string in python"
print(string.rpartition("in"))
# ("sample in string ", "in", " python")


# Case : separator is not found

string : str = "sample python string"
print(string.rpartition("in"))
# ("", "", "sample python string")


# Case : the separator provided is an empty string

string : str = "sample string"
print(string.rpartitionn(""))
# ValueError: empty separator