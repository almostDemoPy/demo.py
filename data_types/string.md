# String
Strings contain texts, or plain texts. They can be alphanumeric or some unicode characters or emojis.

Strings are declared with enclosing ` '' ` single-quotes or ` "" ` double-quotes.
```py
sample : str = "hello world"

>>> print(sample)
"hello world"

>>> type(sample)
<class 'str'>
```


## Formatted Strings or F-Strings
F-Strings are declared with the ` f ` prefix before the opening quotation mark. This allows in-place placeholders, an easier way of than using the ` format() ` method.
```py
sample : str = f""
```

Similar to ` format() ` method, placeholders are in place and does not need placeholder indexing. Placeholders are denoted by enclosing ` {} ` curly braces.
```py
name : str = "demoutrei"

>>> print(f"Hi, my name's {name}")
"Hi, my name's demoutrei"
```

## String Indexing
Similar to list indexing, indexing a string will return a single character. Syntax for indexing a string is denoted by enclosing ` [] ` square brackets. String indexing starts at ` 0 ` and ends at ` n - 1 `, where ` n ` is the length of the string. In case of negative integers, ` -n ` will start from the end of the string, where ` n ` is the ` n `th character starting from the end of the string.
```py
sample : str = "hello world"

>>> sample[0]
"h"

>>> sample[5]
" "

>>> sample[-1]
"d"
```

## String Slicing
Similar to list slicing, the syntax for string slicing is as follows:
```py
[start : end : step]
```
where ` start ` is the start of the slice ( defaults to ` 0 `), ` end ` is the end of the slice ( defaults to ` -1 ` or end character of the string ), and ` step ` determines the interval to take per character.

**Example**
```py
sample : str = "hello world"

>>> sample[2:]
"llo world"

>>> sample[2:8]
"llo wo"

>>> sample[::2]
"hlowrd"
```


## String Methods


### ` capitalize() `
Returns a copy of the string with the first letter capitalized

**Example**
```py
sample : str = "hello world"

>>> sample.capitalize()
"Hello world"
```


### ` casefold() `
Converts the string to lowercase

**Example**
```py
sample : str = "HELLO World"

>>> sample.casefold()
"hello world"
```


### ` center(length : int, fillchar : Optional[str] = " ") `
Returns a new padded string with the specified character

**Parameters**:
- **length** : ` int ` = length of the string after padding
- **fillchar** : Optional[` str `] = character to fill in the padding. Defaults to ` " " ` space

**Example**
```py
sample : str = "hello"

>>> sample.center(9)
"  hello  "

>>> sample.center(9, "*")
"**hello**"
```


### ` count(substring : str, start : Optional[str], end : Optional[int]) `
Returns the number of occurences of a substring inside the string

**Parameters**:
- **substring** : ` str ` = substring whose count is to be taken
- **start** : Optional[` int `] = start of the search. Defaults to ` 0 `
- **end** : Optional[` int `] = end of the search. Defaults to ` -1 ` or end of the string

**Example**:
```py
sample : str = "hello world"

>>> sample.count("l")
3
```


### ` encode(encoding : str, errors : Optional[Literal["strict", "ignore", "replace", "xmlcharrefreplace", "backslashreplace", "namereplace"]]) `
Convert the string into a collection of bytes

**Parameters**:
- **encoding** : ` str ` = encoding on the basis of which it has to be performed
- **errors** : Optional[` str `] = decides how to handle the error if they occur. There are six types of error response:
  - **strict** - default response which raises a ` UnicodeDecodeError ` exception on failure
  - **ignore** - ignores the unencodable unicode from the result
  - **replace** - replaces the unencodable unicode to a question mark
  - **xmlcharrefreplace** - inserts XML character reference instead of unencodable unicode
  - **backslashreplace** - inserts a ` \uNNNN ` escape sequence instead of unencodable unicode
  - **namereplace** - inserts ` \N{...} ` escape sequence instead of unencodable unicode

**Example**
```py
sample : str = "¶"

>>> sample.encode("utf-8")
b'\xc2\xb6'

sample : str = "123-¶"

>>> sample.encode("ascii", errors = "ignore")
b'123-'
```


### ` endswith(suffix : str, start : Optional[int], end : Optional[int]) `
Returns a boolean if the string ends with the given suffix

**Parameters**:
- **suffix** : ` str ` = a substring to be checked at the end of the string
- **start** : Optional[` int `] = start of the search. Defaults to ` 0 `
- **end** : Optional[` int `] = end of the search. Defaults to ` -1 ` or end of the string

**Example**
```py
sample : str = "hello world"

>>> sample.endswith("world")
True

>>> sample.endswith("WORLD")
False
```


### ` expandtabs(tabsize : Optional[int] = 8) `
Substitutes the ` \t ` escape sequence with the specified amount of ` tabsize ` spaces

**Parameters**:
- **tabsize** : Optional[` int `] = amount of spaces to be substituted with ` \t ` escape sequence. Defaults to ` 8 ` spaces

**Example**
```py
sample : str = "hello\tworld"

>>> sample.expandtabs()
"hello        world"

>>> sample.expandtabs(2)
"hello  world"
```


### ` find(substring : str, start : Optional[int], end : Optional[int]) `
Returns the lowest index of the specified substring in the string if found, otherwise returns ` -1 `

**Parameters**:
- **substring** : ` str ` = the substring to look for
- **start** : Optional[` int `] = starting index of the search. Defaults to ` 0 `
- **end** : Optional[` int `] = ending index of the search. Defaults to ` -1 ` or end of the string

**Example**
```py
sample : str = "hello world"

>>> sample.find("lo")
3

>>> sample.find("hi")
-1
```


### ` format_map(map : Dict[str, Any]) `
Format a string by returning a dictionary key's value

**Parameters**:
- **map** : Dict[` str `, Any] = input dictionary

**Example**
```py
sample : Dict[str, Any] = {
  "name" : "demo",
  "language" : "Python"
}

>>> "Hi, I'm {name} and I code in {language}".format_map(sample)
"Hi, I'm demo and I code in Python"
```

### ` format(value : Any, ...) `
Creates a formatted string

Syntax for the placeholders are denoted by enclosing ` {} ` curly braces. Placeholders may contain nothing, an integer denoting the position of its value, or a name of a keyword argument from the method.

**Parameters**:
- **value** : Any = an integer, floating-point numeric constant, string, characters, or variables

**Example**
```py
>>> "hello {}".format("world")
"hello world"

>>> "I bought {0} {1}".format(5, "apples")
"I bought 5 apples"

>>> "Coding in {language} is {}".format("fun", language = "Python")
"Coding in Python is fun"
```

#### Type Specifying
Type specifiers are denoted by the ` % ` percent symbol. There are a few type specifiers, namely:
- ` %s ` - string conversion
- ` %c ` - character conversion
- ` %i ` - signed decimal integer
- ` %d ` - signed decimal integer ( base-10 )
- ` %u ` - unsigned decimal integer
- ` %f ` - floating-point display
- ` %o ` - octal integer
- ` %b ` - binary number
- ` %o ` - octal number
- ` %x ` - hexadecimal with lowercase letters after 9
- ` %X ` - hexadecimal with uppercase letters after 9
- ` %e ` - exponent notation

**Example**
```py
>>> "%s" % "hello world"
"hello world"

>>> "%c" % "a"
"a"

>>> "%i" % -1_000
"-1000"

>>> "%d" % 1_000
"1000"

>>> "%u" % 1_000
"1000"

>>> "%f" % 0.50
"0.50"
```

#### Formatting with Colons
You can further modify your variables in strings with colons. Modifiers may differ on the type of the variable.

**Example**
```py
>>> "{:.2f}".format(10)
"10.00"
```

#### Generating Spaces
Empty spaces can be added to the end of the string if the given integer exceeds the length of the string.

**Example**
```py
>>> "{:10}".format("python")
"python    "
```

#### Padding Substitutions
Texts can be aligned left, right, or centered. The syntax for it is as follows:
- ` < ` - align left
- ` ^ ` - align center
- ` > ` - align right

**Example**
```py
>>> "{:<10}".format("python")
"python    "

>>> "{:^10}".format("python")
"  python  "

>>> "{:>10}".format("python")
"    python"
```

#### Using a Dictionary
Dictionaries can be used in formatting strings as well. These should be unpacked when in the method.

**Example**
```py
>>> "Coding in {language} is {adjective}".format(**{"adjective": "fun", "language": "Python"})
"Coding in Python is fun"
```


### ` index(substring : str, start : Optional[int], end : Optional[int]) `
Return the index of the first occurence of the substring in the string

**Parameters**:
- **substring** : ` str ` = the substring to look for
- **start** : Optional[` int `] = start of the search. Defaults to ` 0 `
- **end** : Optional[` int `] = end of the search. Defaults to ` -1 ` or end of the string

**Example**
```py
sample : str = "hello world"

>>> sample.index("lo")
3
```


### ` isalnum() `
Check if all characters in the string are either alphabet or numeric

**Example**
```py
>>> "abc".isalnum()
True

>>> "123".isalnum()
True

>>> "abc123".isalnum()
True

>>> "abc 123".isalnum()
False

>>> "abc_123".isalnum()
False
```

> **NOTE**
> 
> ` _ ` Underscores and ` " " ` empty spaces are not considered alphanumeric.


### ` isalpha() `
Check whether all characters in the string are alphabet

**Example**
```py
>>> "abc".isalpha()
True

>>> "123".isalpha()
False

>>> " ".isalpha()
False

>>> "_".isalpha()
False
```


### ` isdecimal() `
Check if all characters in a string are decimal

**Example**
```py
>>> "123".isdecimal()
True

>>> "1/2".isdecimal()
True

>>> "abc".isdecimal()
False
```


### ` isdigit() `
Check if all characters in a string are digits

**Example**
```py
>>> "123".isdigit()
True

>>> "1²3".isdigit()
True

>>> "1/2".isdigit()
False

>>> "½".isdigit()
False
```


### ` isidentifier() `
Check if a string is a valid identifier.

A string is considered a valid identifier if:
- it only consists of alphanumeric characters and underscore
- doesn't start with a space or a number

**Example**
```py
>>> "abc".isidentifier()
True

>>> "abc123".isidentifier()
True

>>> "abc_123".isidentifier()
True

>>> "abc 123".isidentifier()
False

>>> "123abc".isidentifier()
False
```


### ` islower() `

Check if all characters in the string are in lowercase

**Example**
```py
>>> "abc123".islower()
True

>>> "Abc123".islower()
False

>>> "ABC123".islower()
False
```


### ` isnumeric() `
Check if all characters in the string are numeric

**Example**
```py
>>> "0123456789".isnumeric()
True

>>> "abc123".isnumeric()
False
```


### ` isprintable() `
Check if all characters in the string are printable or the string is empty.

Printable characters are:
- Digits - ` 0123456789 `
- Uppercase Letters - ` ABCEDFGHIJKLMNOPQRSTUVWXYZ `
- Lowercase Letters - ` abcdefghijklmnopqrstuvwxyz `
- Punctuation Characters - ` !"#$%&'()*+, -./:;?@[\]^_{|}~ `
- Space - `   `

**Example**
```py
>>> "hello world".isprintable()
True

>>> "".isprintable()
True

>>> "hello\nworld".isprintable()
False
```


### ` isspace() `
Check if all characters in the string are whitespace characters.

Whitespace characters are:
- Space - `   `
- Horizontal tab - ` \t `
- Newline - ` \n `
- Vertical tab - ` \v `
- Feed - ` \f `
- Carriage return - ` \r `

**Example**
```py
>>> "".isspace()
True

>>> "\n\n:.isspace()
True

>>> "hello\tworld".isspace()
False
```


### ` istitle() `
Check if all the words in the string are title-cased.

A string is title-cased when all words begin with an uppercase character and the remaining characters are in lowercase.

**Example**
```py
>>> "Hello World".istitle()
True

>>> "123 World".istitle()
True

>>> "Hello world".istitle()
False
```


### ` isupper() `
Check whether all characters in the string are in uppercase

**Example**
```py
>>> "HELLO WORLD".isupper()
True

>>> "Hello World".isupper()
False

>>> "123".isupper()
False
```


### ` join(iterable : Iterable) `
Joins items of the iterable separated by the string separator

**Parameters**:
- **iterable** : Iterable = containing the strings to join with the separator

**Example**
```py
sample : List[str] = ["hello", "world", "python"]

>>> " ".join(sample)
"hello world python"

>>> "-".join(sample)
"hello-world-python"
```


### ` lower() `
Converts all characters to lowercase

**Example**
```py
sample : str = "HELLO WORLD"

>>> sample.lower()
"hello world"
```


### ` lstrip(characters : Optional[str] = " ") `
Returns a copy of the string with the leading characters removed matching the characters provided in ` characters ` parameter

**Parameters**:
- **characters** : Optional[` str `] = string of characters to remove as leading characters. Defaults to ` " " ` space.

**Example**
```py
>>> "   hello world   ".lstrip()
"hello world   "

>>> "abababababahello worldbababbab".lstrip("ab")
"hello worldbababbab"
```


### ` maketrans(replaced : str, replacements : str, deleted : Optional[str]) `
Constructs a transition table [ of a list of characters ] that need to be replaced or deleted from the original string.

**Parameters**:
- **replaced** : ` str ` = set of characters that need to be replaced
- **replacements** : ` str ` = set of characters with which the characters need to be replaced with. The characters must match the position of the character in ` replaced ` that it needs to replace with.
- **deleted** : Optional[` str `] = set of characters that needs to be deleted

**Example**
```py
sample : str = "hello world"

>>> sample.maketrans("hlo", "nod")
{104: 110, 108: 111, 111: 100}
```


### ` partition(separator : str) `
Splits the string at the first occurence of the separator

**Parameters**:
- **separator** : ` str ` = substring that separates the string

**Example**
```py
sample : str = "hello world python"

>>> sample.partition("world")
("hello ", "world", " python")
```


### ` replace(old : str, new : str, count : Optional[int]) `
Replace all occurences of asubstring with another substring

**Parameters**:
- **old** : ` str ` = substring you want to replace
- **new** : ` str ` = substring which would replace the ` old ` substring
- **count** : Optional[` int `] = number of times you want to replace. Defaults to all occurences.

**Example**
```py
sample : str = "hello world"

>>> sample.replace("l", "m")
"hemmo wormd"
```


### ` rfind(substring : str, start : Optional[int], end : Optional[int]) `
Returns the right-most index of the substring if found in the string, otherwise it returns ` -1 `

**Parameters**:
- **substring** : ` str ` = the substring to look for
- **start** : Optional[` int `] = starting index of the search. Defaults to ` 0 `
- **end** : Optional[` int `] = ending position of the search. Defaults at ` -1 ` or the end of the string

**Example**
```py
sample : str = "hello world"

>>> sample.rfind("l")
9
```


### ` rindex(substring : str, start : Optional[int], end : Optional[int]) `
Returns the highest index of the substring inside the string

**Parameters**:
- **substring** : ` str ` = substring to search for
- **start** : Optional[` int `] = starting index of the search. Defaults to ` 0 `
- **end** : Optional[` int `] = ending position of the search. Defaults at ` -2 ` or end of the string

**Example**
```py
sample : str = "hello world"

>>> sample.rindex("l")
9
```


### ` rpartition(separator : str) `
Splits the string into three parts, starting from the right side: left-hand side of the separator, the separator, and the right-hand side of the separator

**Parameters**:
- **separator** : ` str ` = string separator

**Example**
```py
sample : str = "sample in string in python"

>>> sample.rpartition("in")
("sample in string ", "in", " python")
```


### ` rsplit(separator : str, max_split : Optional[int]) `
Returns a list of strings after breaking the original string starting from the right side by the specified separator

**Parameters**:
- **separator** : ` str ` = substring to split the original string. Defaults to ` " " ` space
- **max_split** : Optional[` int `] = maximum splits to process. Defaults to ` None `

**Example**
```py
sample : str = "hello world python"

>>> sample.rsplit(" ", 1)
["hello world", "python"]

>>> smaple.rsplit(" ")
["hello", "world", "python"]
```


### ` rstrip(chars : Optional[str]) `
Returns a copy of the string with the trailing characters removed

**Parameters**:
- **chars** : Optional[` str `] = string of characters that are to be removed. Defaults to ` " " ` space

**Example**
```py
sample : str = "ababbabahello worldbababa"

>>> sample.rstrip("ab")
"ababbabahello world"
```


### ` splitlines(keepends ; Optional[bool]) `
Splits the lines at line boundaries

` splitlines() ` splits on the following line boundaries:
- ` \n ` - Line Feed
- ` \r ` - Carriage Return
- ` \x1c ` - File Separator
- ` \x1d ` - Group Separator
- ` \x85 ` - Next Line
- ` \v ` or ` \x0b ` - Line Tabulation
- ` \f ` or ` \x0c ` - Form Feed
- ` \u2028 ` - Line Separator
- ` \u2029 ` - Paragraph Separator

**Parameters**:
- **keepends** : Optional[` bool `] = when set to ` True `, line breaks are included in the resulting list. Defaults to ` False `

**Example**
```py
sample : str = "hello\nworld"

>>> sample.splitlines()
["hello", "world"]

>>> smaple.splitlines(True)
["hello\n", "world"]
```


### ` startswith(prefix : str, start : Optional[int], end : Optional[int]) `
Checks if the string starts with a specific prefix

**Parameters**:
- **prefix** : ` str ` = substring to check for
- **start** : Optional[` int `] = starting index of the search. Defaults to ` 0 `
- **end** : Optional[` int `] = ending position of the search. Defaults to ` -1 ` or end of the string

**Example**
```py
sample : str = "hello world"

>>> sample.startswith("hell")
True
```


### ` strip(chars : str) `
Strips both leading and trailing characters from the string

**Parameters**:
- **chars** : ` str ` = string specifying the set of characters to be removed. Defaults to ` " " ` space

**Example**
```py
sample : str = "   hello world   "

>>> sample.strip()
"hello world"
```


### ` swapcase() `
Swaps the case of the characters of the string from lowercase to uppercase and vice versa

**Example**
```py
sample : str = "Hello World"

>>> sample.swapcase()
"hELLO wORLD"
```


### ` title() `
Converts every word in the string to title-case

**Example**
```py
sample : str = "hello world"

>>> sample.title()
"Hello World"
```


### ` translate(table : Dict[str, str], deleted : Optional[str]) `
Translate the characters using a translation table

**Parameters**:
- **table** : Dict[` str `, ` str `] = the translation table to be used
- **deleted** : Optional[` str `] = string specifying the set of characters to be deleted

**Example**
```py
sample : str = "hello world"

>>> sample.translate(sample.maketrans("hlo", "nod"))
"neood wdrod"
```


### ` upper() `
Converts all characters in the string to uppercase

**Example**
```py
sample : str = "hello world"

>>> sample.upper()
"HELLO WORLD"
```


### ` zfill(length : int) `
Returns a copy of the string with ` 0 ` characters padded to the left side of the original string

**Parameters**:
- **length** : ` int ` = length of the resulting string

**Example**
```py
sample : str = "python"

>>> sample.zfill(10)
"0000python"
```