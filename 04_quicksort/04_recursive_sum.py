def recursive_sum(list):
  if list == []:
    return 0
  return list[0] + recursive_sum(list[1:])

if __name__ == "__main__":
  test_array = [1, 2, 3, 4]
  print(recursive_sum(test_array))
