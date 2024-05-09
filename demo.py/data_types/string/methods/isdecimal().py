"""

str.isdecimal()

- Check if all characters in a string are decimal

"""

string : str = "123"
print(string.isdecimal())
# True


string : str = "abc"
print(string.isdecimal())
# False


string : str = "abc123"
print(string.isdecimal())
# False


string : str = "1/2"
print(string.isdecimal())
# False