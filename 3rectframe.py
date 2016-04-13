#!/usr/bin/python

"""
Write a function that takes a list of strings and prints them, one per line, in
a rectangular frame. For example, the list
["Hello", "World", "in", "a", "frame"] gets printed as:
  *********
  * Hello *
  * World *
  * in    *
  * a     *
  * frame *
  *********
"""

list1 = ["Hello", "World", "in", "a", "frame"]
list2 = ["one", "two", "three", "onomatopoeia"]
list3 = ["a"]
list4 = ["xyz"]

def print_frame(word_list):
  print(word_list)

  # find the width of the frame (based on the longest word)
  frame_width = len(max(word_list, key=len))

  # print(the top of the frame
  print('*' * (frame_width+4))

  # print the words in the list
  for word in word_list:
    # strictly speaking, the word and width params don't have to be explicit
    print('* {word:<{width}} *'.format(word=word,width=frame_width))

  # print(the bottom of the frame
  print('*' * (frame_width+4))
  print('')

print_frame(list1)
print_frame(list2)
print_frame(list3)
print_frame(list4)

