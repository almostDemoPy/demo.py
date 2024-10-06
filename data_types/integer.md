# Integer
Integers are, or can be, whole numbers. Can be positive or negative. Integers are not declared with a ` . ` decimal point and represented as a whole.
```py
sample : int = 123

>>> sample
123

>>> type(sample)
<class 'int'>
```

Unlike Javascript, or any other languages, Python can handle pretty large integers.
```py
sample : int = 7193209397147042915750149147

>>> sample
7193209397147042915750149147
```

> **TIP**
> ` _ ` Underscores can be used for thousand separators. This makes it easier to read big integers.
> ```py
> sample : int = 1_000
> 
> >>> sample
> 1000
> ```