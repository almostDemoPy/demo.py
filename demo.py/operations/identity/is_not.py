"""

x is not y

- Returns True if both operands are not identical in memory

"""

a = 10
b = a
print(a is not b)
# False


a = 10
b = 10
print(a is not b)
# False


a = 10
b = 20
print(a is not b)
# True