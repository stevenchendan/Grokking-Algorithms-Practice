def recursive_count(list):
  if list == []:
    return 0
  return 1 + recursive_count(list[1:])


if __name__ == "__main__":
  test_array = [1, 2, 3, 4]
  print(recursive_count(test_array))