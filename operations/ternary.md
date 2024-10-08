# Ternary
Ternaries are conditional expressions that evaluates something based on a condition being ` True ` or ` False `

**Syntax**
```py
<on_true> if <condition> else <on_false>
```

**Equivalent to**:
```py
if condition:
  on_true
else:
  on_false
```

**Example**
```py
a : int = 10
b : int = 10

>>> "equal" if a == b else "not equal"
"equal"
```