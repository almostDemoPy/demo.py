"""

str.replace(
  old : str,
  new : str,
  count : Optional[int]
)

- Replace a subtring with another substring

===============================================================

Parameters :

old : str = substring you want to replace

new : str = substring which would replace the old one

count : Optional[str] = number of times you want to replace

"""

string : str = "extreme string"
print(string.replace("extreme", "sample"))
# "sample string"


string : str = "abbcccdddd"
print(string.replace("c", "e"))
# "abbeeedddd"