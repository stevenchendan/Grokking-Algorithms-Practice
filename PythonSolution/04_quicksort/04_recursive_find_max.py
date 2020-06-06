def max_number(list):
  #handle edge case
  if len(list) == 0:
    return None
  #base case
  if len(list) == 1:
    return list[0]
  #recursive case
  else:
    #
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

if __name__ == "__main__":
  print(max_number([2, 100, 101, 200]))