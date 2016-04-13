#!/usr/bin/python

"""
Problem:
- Given a fraction, print its decimal representation
- If the result is a repeating decimal, print the repeating portion in brackets
- Examples:
  2/3 = 0.[6]
  3/4 = 0.75
  7/11 = 0.[63]
  7/12 = 0.58[3]
  3/13 = 0.[230769]
  5/28 = 0.17[857142]
  5/29 = 0.[1724137931034482758620689655]

Assumptions:
- Fraction will be between 0 and 1 inclusive
"""

import sys

n = sys.argv[1]
d = sys.argv[2]

remainder_set = set()


