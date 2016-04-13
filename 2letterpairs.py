#!/usr/bin/python

from collections import defaultdict

# generate the pairs in the string
def get_pairs(str):
  for i in xrange(len(str)-1):
    yield str[i]+str[i+1]


# open file
file_in = raw_input('File name: ')
try:
  with open(file_in,'r') as f:
    paragraph = f.read().strip().lower().translate(None,'!@#$%^&*()-_=+/?.><,0123456789 ')
except IOError:
  print 'file does not exist'
  exit(1)

print paragraph
print 'done'

pairs = defaultdict(int) # maps string > int
total_pairs = 0 # not a unique count

# count the pairs
for pair in get_pairs(paragraph):
  total_pairs += 1
  pairs[pair] += 1


# get the top 20 keys by count
print("{} total pairs".format(total_pairs))

top_pairs = sorted(zip(pairs.values(), pairs.keys()), reverse=True)[:20]

# print the top 20
for p in top_pairs:
  print("{} {:.2%}".format(p[1],1.0*p[0]/total_pairs))


