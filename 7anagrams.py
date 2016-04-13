#!/usr/bin/python

import sys

w1 = sys.argv[1]
w2 = sys.argv[2]

print(w1)
print(w2)

print(sorted(list(w1)) == sorted(list(w2)))
