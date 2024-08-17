# VARIABLES

# String

string : str = "hello world"


# Integer

number : int = 123


# Float

number : float = 123.0


# List

sample : list[int] = [1, 2, 3]
sample : list[str] = ["hello world"]
sample : list[str | int] = [123, "hello world"]


# Dictionary

sample : dict[str, int] = {"1": 1, "2": 2, "3": 3}
sample : dict[int, int] = {1: 1, 2: 2, 3: 3}


# Tuple

sample : tuple[int] = (1, 2, 3)


# Integer OR Float

number : int | float = 123.0


# String OR List of Strings

sample : str | list[str] = ...