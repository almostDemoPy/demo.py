"""

str.expandtabs(
  tabsize : Optional[int]
)

- specifies the amount of space to be substituted with "\t" symbol


Parameters :

tabsize : Optional[int] = amount of spaces to be substituted with "\t". defaults to 8 spaces

"""

string : str = "sample\tstring"
print(string.expandtabs())

# Output :
# sample        string


string : str = "sample\tstring"
print(string.expandtabs(4))

# Output :
# sample    string