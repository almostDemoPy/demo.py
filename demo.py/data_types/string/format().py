"""

str.format(
  value : Any
)

- Create formatted strings

Parameters :
  value : Any = an integer, floating point numeric constant, string, characters, or variables

"""

string : str = "Hello {}"
print(string.format("world"))
# "Hello world"


# multiple placeholders :

string : str = "I bought {0} {1}"
print(string.format(5, "apples"))
# "I bought 5 apples"


# positional and keyword placeholders

string : str = "{name} is coding in {}"
print(string.format("Python", name = "demo"))
# "demo is coding in Python"


# Type Specifying :

# %s - string conversion
string : str = "%s"
print(string % "hello world")
# "hello world"

# %c - character conversion
string : str = "%c"
print(string % "a")
# "a"

# %i - signed decimal integer
string : str = "%i"
print(string % -1_000)
# "-1000"

# %d signed decimal integer(base-10)
string : str = "%d"
print(string % 1_000)
# "1000"

# %u - unsigned decimal integer
string : str = "%u"
print(string % 1_000)
# "1000"

# %f - floating-point display
string : str = "%f"
print(string % 0.50)
# "0.50"

# other useful type specifying :
# %o - octal integer
# %b - binary number
# %o - octal number
# %x - hexadecimal with lowercase letters after 9
# %X - hexadecimal with uppercase letters after 9
# %e - exponent notation


# formatting symbols with colons :

string : str = "{:.2f}"
print(string.format(10))
# "10.00"


# Generating Spaces

string : str = "{:20}"
print(string.format("hello world"))
# "hello world"


# Padding Substitutions

# < : left-align
# ^ : center text
# > : right-align

string : str = "{0:<20}"
print(string.format("hello world"))
# "hello world"

string : str = "{:^20}"
print(string.format("hello world"))
# "     hello world     "

string : str = "{:>20}"
print(string.format("hello world"))
# "         hello world"


# Using a dictionary

string : str = "Hello ! My name is {name} and I'm {age} years old !"
demo : dict = {
  "name" : "demo",
  "age" : 18
}
print(string.format(**demo))
# "Hello ! My name is demo and I'm 18 years old !"