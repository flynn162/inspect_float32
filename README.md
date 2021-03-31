Prints floating point numbers in binary. Usage:

```python3
$ python3 -i inspect_float32.py
>>> show('0.25')
s      exp            significants
0 01111101 00000000000000000000000  = 0.25
+       -2
>>> show('0.3')  # example of a non-terminating expansion
s      exp            significants
0 01111101 00110011001100110011010  = 0.30000001192092896
+       -2
>>> show('3.14159')
s      exp            significants
0 10000000 10010010000111111010000  = 3.141590118408203
+        1
```

SPDX-License-Identifier: MIT
