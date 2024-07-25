"""

x * y

- Multiply two operands

"""

# float * float

a : float = 1.0
b : float = 1.5
print(a * b)
# 1.5

# -------------------------------------------------------------

# float * integer

a : float = 1.0
b : int = 2
print(a * b)
# 2.0

# =============================================================

# integer * float

a : int = 2
b : float = 2.5
print(a * b)
# 5.0

# -------------------------------------------------------------

# integer * integer

a : int = 2
b : int = 5
print(a * b)
# 10

# =============================================================

# list * int

a : list[int] = [1, 2]
b : int = 2
print(a * b)
# [1, 2, 1, 2]

# =============================================================

# string * integer

a : str = "python"
b : int = 2
print(a * b)
# "pythonpython"