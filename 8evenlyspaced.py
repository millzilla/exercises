#!/usr/bin/python

import sys

nums = sorted([int(i) for i in sys.argv[1:]])

print(nums[1]-nums[0] == nums[2]-nums[1])


