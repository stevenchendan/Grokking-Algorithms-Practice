def recursive_sum(list):
  total = 0
  if list == []:
    return 0
  return list[0] + recursive_sum(list[1:])

print(recursive_sum([1, 2, 3, 4]))
