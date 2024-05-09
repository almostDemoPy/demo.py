"""

str.isalnum()

- Check if all characters in the string are either alphabet or numeric.

"""

string : str = "python"
print(string.isalnum())
# True

string : str = "123"
print(string.isalnum())
# True

string : str = "demo456"
print(string.isalnum())
# True


# Case : whitespaces

string : str = "hello world"
print(string.isalnum())
# False


# Case : underscores

string : str = "abc_123"
print(string.isalnum())
# False