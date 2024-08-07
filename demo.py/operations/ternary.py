"""

on_true if condition else on_false

- Conditional expressions that evaluates something based on
    a condition being True or False


Equivalent to :

if condition:
  on_true
else:
  on_false

"""

a = b = 10
print(
  "equal" if a == b else "not equal"
)
# "equal"


a, b = 10, 15
print(
  "equal" if a == b else "not equal"
)
# "not equal"