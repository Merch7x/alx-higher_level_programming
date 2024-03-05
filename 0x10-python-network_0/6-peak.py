#!/usr/bin/python3
"""Sorts a list of intgers to find
largest
"""
def find_peak(list_of_integrs):
  """Sorts a list"""
  if list_of_integrs:
    list_of_integrs.sort(reverse=True)
    return list_of_integrs[0]
  else:
    return None

# print(find_peak([1, 2, 4, 6, 3]))
# print(find_peak([4, 2, 1, 2, 3, 1]))
# print(find_peak([2, 2, 2]))
# print(find_peak([]))
# print(find_peak([-2, -4, 2, 1]))
# print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))