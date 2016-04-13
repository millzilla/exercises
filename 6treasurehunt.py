#!/usr/bin/python

treasure_map = [
  [34,21,32,41,25],
  [14,42,43,14,31],
  [54,45,52,42,23],
  [33,15,51,31,35],
  [21,52,33,13,23]
]

r = 0
c = 0
next_r = -1
next_c = -1

# tens = row
# ones = col

treasure_found = False

for i in treasure_map:
  print i

while not treasure_found:
  coords = list(str(treasure_map[r][c]))
  next_r = int(coords[0])-1
  next_c = int(coords[1])-1

  if r == next_r and c == next_c:
    treasure_found = True
  else:
    r = next_r
    c = next_c

print('treasure at r={},c={}'.format(r+1, c+1))
