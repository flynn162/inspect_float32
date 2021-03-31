#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""
Prints floating point numbers in binary. Usage:

$ python3 -i inspect_float32.py
>>> show('0.25')
>>> show('0.3')  # example of a non-terminating expansion
>>> show('3.14159')
"""

import numpy as np
import sys

def show(to_float32):
    view_float(np.float32(to_float32))

def view_float(flt):
    b = np.binary_repr(flt.view(np.uint32)).rjust(32, '0')
    sign = b[0]
    exponent = b[1:1+8]
    significants = b[9:]
    print('s', 'exp'.rjust(8, ' '), 'significants'.rjust(23, ' '))
    print(sign, exponent, significants, end=' ')
    print(' =', flt.astype(str))
    print('+' if sign == '0' else '-', end=' ')
    unbiased_exponent = int(exponent, base=2) - 127
    if unbiased_exponent == 128:
        if int(significants, 2) == 0:
            print('infinity')
        else:
            print('NaN'.rjust(8, ' '))
    else:
        print(str(unbiased_exponent).rjust(8, ' '))

def print_help():
    print(__doc__.strip(), file=sys.stderr)

if __name__ == '__main__' and not sys.flags.interactive:
    print_help()
    sys.exit(1)
