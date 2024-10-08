# Bitwise

## Bitwise-AND Operation
Each bit of the output is 1 if the corresponding bit of x and of y is 1, otherwise it's 0

**Example**
```py
>>> 10 & 6
2
```

**Explanation**
```
  1010 | 10
& 0110 |  6
------ | --
  0010 |  2
```


## Bitwise Left Shift Operation
Returns the ` x ` with the bits shifted to the left by ` y ` places ( and new bits on the right-hand sid are zeroes ). This is the same as ` 2 ** y `

**Example**
```py
>>> 5 << 2
20
```

**Explanation**
```
   0000 0101 |  5
<<        00 |  2
------------ | --
   0001 0100 | 20
```


## Bitwise-NOT Operation
Returns the complement of ` x ` - the number you get by switching each ` 1 ` for a ` 0 ` and each ` 0 ` for a ` 1 `. This is the same as ` -x - 1 `

**Example**
```py
>>> ~10
-11
```

**Explanation**
```
   1010 |  10
+  0001 |   1
--------|----
~  1011 |  11
--------|---
  -1011 | -11
```


## Bitwise-OR Operation
Each bit of the output is ` 0 ` if the corresponding bit of ` x ` and of ` y ` is ` 0 `, otherwise ` 1 `

**Example**
```py
>>> 10 | 4
14
```

**Explanation**
```
  1010 | 10
| 0100 |  4
-------|---
  1110 | 14
```


## Bitwise Right Shift Operation
Returns ` x ` with the bits shifted to the right by ` y ` places. This is the same as dividing ( floor ) ` x ` by ` 2 ** y `

**Example**
```py
>>> 10 >> 2
2
```

**Explanation**
```
   1010 | 10
>> 00   |  2
--------|---
   0010 |  2
```


## Bitwise-xOR Operation
Each bit of the output is the same as the corresponding bit in ` x ` if that bit in ` y ` is ` 0 `, and it's the complement of the bit in ` x ` if that bit in ` y ` is ` 1 `

**Example**
```py
>>> 10 ^ 7
13
```

**Explanation**
```
  1010 | 10
^ 0111 |  7
-------|---
  1101 | 13
```