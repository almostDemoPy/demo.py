"""

global

- Used to access and modify a variable in the
    global scope

"""

x : int = 5

def function() -> None:
  x += 5
  # UnboundLocalError: cannot access local
  #     variable 'x' where it is not
  #     associated with a value

function()


# ===========================================


x : int = 5

def function() -> None:
  global x
  x += 5

function()
print(x)
# 10