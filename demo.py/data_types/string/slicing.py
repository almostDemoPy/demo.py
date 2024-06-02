"""

str[start : stop : step]


Options :

start : Optional[int] = the index of the string to start
    slicing, defaults to 0

stop : Optional[int] = position of the string to stop slicing,
    defaults to the length of the string

step : Optional[int] = how many steps per iter to take in slicing,
    defaults to 1

"""

# Case : start is only specified

# str[start:]
# - gets the substring from the start index up to the end of
#     the string

string : str = "sample string"
print(string[2:])
# "mple string"

string : str = "sample string"
print(string[-6:])
# "string"


# Case : stop is only specified

# str[:end]
# - gets the substring from the 0th index up to the stop
#     position

string : str = "sample string"
print(string[:6])
# "sample"

string : str = "sample string"
print(string[:-5])
# "sample s"


# Case : step is only specified

# str[::step]
# - gets the characters every step of the string starting from
#     the first character

string : str = "sample string"
print(string[::2])
# "sml tig"

string : str = "sample string"
print(string[::-2])
# "git lms"


# Case : both start and stop are specified

# str[start:stop]
# - gets the characters from start index up to the stop index
#     with step 1

string : str = "sample string"
print(string[2:6])
# "mple"

string : str = "sample string"
print(string[3:-2])
# "ple stri"