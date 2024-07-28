"""

x + y

- Add two operands

"""

# float + float

a : float = 1.0
b : float = 0.5
print(a + b)
# 1.5

# -------------------------------------------------------------

# float + integer

a : float = 1.0
b : int = 1
print(a + b)
# 2.0

# =============================================================

# integer + float

a : int = 1
b : int = 1.0
print(a + b)
# 2.0

# -------------------------------------------------------------

# integer + integer

a : int = 2
b : int = 3
print(a + b)
# 5

# =============================================================

# list + list

a : list[int] = [1, 2, 3]
b : list[int] = [4, 5, 6]
print(a + b)
# [1, 2, 3, 4, 5, 6]

# =============================================================

# string + string

a : str = "hello "
b : str = "world"
print(a + b)
# "hello world"