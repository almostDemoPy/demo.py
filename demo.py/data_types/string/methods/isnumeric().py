"""

str.isnumeric()

- Check if all characters in a string are numeric

"""

string : str = "1234567890"
print(string.isnumeric())
# True


string : str = "abc123"
print(string.isnumeric())
# False


string : str = "abc"
print(string.isnumeric())
# False