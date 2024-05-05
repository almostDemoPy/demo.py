"""

str.islower()

- Check if all characters in the string are lowercase

"""

string : str = "abc123"
print(string.islower())
# True


string : str = "ABC123"
print(string.islower())
# False


string : str = "Abc123"
print(string.islower())
# False