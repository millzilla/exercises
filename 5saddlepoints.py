#!/usr/bin/python

arr1 = [
    [1,2,3,9,5],
    [3,4,5,9,1],
    [1,5,6,8,7],
    [2,6,1,9,5],
    [4,7,8,9,7]
]

arr2 = [
    [2,6,1,3,5],
    [1,5,6,8,7],
    [3,4,5,2,1],
    [4,7,8,9,7],
    [1,2,3,4,5]
]

arr3 = [
    [4,7,8,9,7],
    [1,2,3,4,5],
    [1,5,6,8,7],
    [3,4,5,2,1],
    [2,6,1,3,5]
]

arr4 = [
    [3,3,6,3,3],
    [3,3,4,3,3],
    [3,3,6,3,3],
    [4,3,6,3,3],
    [4,1,4,1,1]
]

def find_saddles(arr):
  num_saddle = 0

  for r in range(5):
    print(arr[r])

  for r in range(5):
    for c in range(5):
      # saddle point if item is largest in row & smallest in column
      #print('row: {}'.format(arr[r]))
      #print('col: {}'.format([i[c] for i in arr]))
      if arr[r][c] >= max(arr[r]) and arr[r][c] <= min([i[c] for i in arr]):
        print('{},{}'.format(r, c))
        num_saddle += 1

  if not num_saddle:
    print('no saddle pts')
  print('')

find_saddles(arr1)
find_saddles(arr2)
find_saddles(arr3)
find_saddles(arr4)
