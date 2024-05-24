"""

str.partition(
  separator : str
)

- Split the string at the first occurence of the separator

===============================================================

Parameters :

separator : str = substring that separates the string

===============================================================

Exceptions :

ValueError : empty separator

"""

string : str = "sample python string"
separator : str = "python"
print(string.partition(separator))
# ("sample ", "python", " string")


# Case : separator is not found in the string

string : str = "sample string"
separator : str = "of"
print(string.partition(separator))
# ("sample string", "", "")


# Case : separator is an empty string

string : str = "sample string"
separator : str = ""
print(string.partition(separator))
# ValueError: empty separator