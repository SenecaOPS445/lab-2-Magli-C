#!/usr/bin/env python3
import sys

arguments = sys.argv


if len(sys.argv) == 3:
    name = sys.argv[1]
    age = sys.argv[2]
    print('Hi ' + sys.argv[1] + ', you are ' + sys.argv[2] + ' years old.')
    sys.exit()
print('Usage: ' + sys.argv[0] + ' name age')