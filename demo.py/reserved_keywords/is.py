"""

is

- Used to check if the left operand references to an object
    in memory

"""


a : int = 5
b : float = 5.0
print(a == b)
# True


a : int = 5
b : float = 5.0
print(a is b)
# False