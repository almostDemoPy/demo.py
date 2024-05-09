"""

str.isdigit()

- Check if all characters in a string are digits

"""

string : str = "123"
print(string.isdigit())
# True


string : str = "abc123"
print(string.isdigit())
# False


# Case : superscript

string : str = "1²3"
print(string.isdigit())
# True


# Case : fraction

string : str = "½"
print(string.isdigit())
# False

string : str = "1/2"
print(string.isdigit())
# False