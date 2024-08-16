"""

variable_name : tuple = value, Optional[values]

Note: A tuple is created when a comma is
    placed after the first value, not by the
    surrounding parentheses.

"""


sample : tuple[int] = 1, 2
print(sample)
# (1, 2)
print(type(sample))
# <class 'tuple'>


sample : tuple[int] = 1,
print(sample)
# (1,)
print(type(sample))
# <class 'tuple'>


sample : tuple[int] = (1)
print(sample)
# 1
print(type(sample))
# <class 'int'>