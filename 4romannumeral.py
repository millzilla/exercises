#!/usr/bin/python

"""
INPUT REQUIREMENTS

Read one or more roman numerals from standard input. Process one line at a time.
Each input line contains only one roman numeral, starting in column one. Assume
the characters are all upper case with no embedded blanks.

OUTPUT REQUIREMENTS

The arabic equivalent of each input roman numeral is displayed on standard
output, starting in column one.

FUNCTIONAL REQUIREMENTS

Here are the arabic equivalents for roman symbols:

   "Basic"                   "Auxiliary"
   I   X    C    M           V   L   D
   1   10   100  1000        5   50  500


   Convert the roman numeral to arabic processing the symbols from left to right
   according to the following rules:

   1. A symbol following one of greater or equal value adds to its value.
      (E.g., XII = 12)

   2. A symbol preceding one of greater value subtracts its value.
      (E.g., IV = 4; XL = 40)

   ERROR HANDLING REQUIREMENTS

   In each of the error conditions below, display the given message and skip the
   numeral and continue processing the next line.

   "Invalid character in input. Valid characters are I,V,X,L,C,D,M."
      Only the listed characters are valid.

   "Invalid numeral: can't subtract auxiliary symbol."
      It is not permitted to subtract an "auxiliary" symbol.
      (CML = 950, not LM; XLV = 45, not VL).

   "Invalid numeral: two consecutive subtractions."
      Can't do two subtractions in a row, thus LIVX is illegal.

   "Invalid numeral: additions don't decrease."
      Additions must decrease, as you go from left to right. Thus, each symbol
      added must have a value equal or less than the last symbol which was added.
      Thus, LIIX is wrong, cause we added L, added I, subtracted I, then try
      to add X.

EXAMPLES

  CML =       M - C + L = 950
  XLV =       L - X + V = 45
  XII =       X + I + I = 12
  XV =        X + V = 15
  MCMIV =     M + M - C + I - V = 1904
  CDXLVIII =  D - C + L - X + V + I + I + I = 448
  MCMXCVIII = M + M - C + C - X + V + I + I + I = 1998

"""

# basically, lookahead = 1, keep track of last operation
# if this numeral is smaller, add
# if it's larger and is not auxiliary, subtract
# otherwise, error

from enum import Enum

NUMERALS = {'I':1,'X':10,'C':100,'M':1000,'V':5,'L':50,'D':500}
BASIC = ['I','X','C','M']
AUX = ['V','L','D']

def get_num_value(numeral):
  if num not in NUMERALS:
    print('Invalid numeral: \'{}\''.format(num))
    exit()
  else
    return NUMERALS[num]

def parse_roman(roman_str):
  pos = 0
  total = 0

  print(roman_str)

  while pos != len(roman_str):
    num = roman_str[pos]
    print(num)

    value = get_num_value(num)

    # figure out if it should be added or subtracted
    # by doing a lookahead
    if pos + 1 != roman_str:
      pass


    pos += 1


  print(total)
