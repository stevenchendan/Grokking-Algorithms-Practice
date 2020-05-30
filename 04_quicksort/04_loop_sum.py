def sum(arr):
  total = 0
  for i in arr:
    total += i
  return total

if __name__ == "__main__":
  test_array = [1, 2, 3, 4]
  print(sum(test_array))