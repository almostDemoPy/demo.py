"""

str.isalpha()

- Check whether all characters in the string are an alphabet

"""

string : str = "abc"
print(string.isalpha())
# True


string : str = "ABC"
print(string.isalpha())
# True


string : str = "123"
print(string.isalpha())
# False


# Case : whitespaces

string : str = "hello world"
print(string.isalpha())
# False