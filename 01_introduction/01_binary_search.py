class Solution():
  def binary_search(list, item):
    
    # handle edge case
    if list == None or len(list) == 0:
      return None
    
    low = 0
    high = len(list) - 1

    while low <= high:
      mid = (low + high) // 2
      guess = list[mid]
      if guess == item:
        return mid
      if guess < item:
        low = mid + 1
      else:
        high = mid - 1
      
    return None


#TODO:write proper test cases

#test
test_array = [1,2,3,4,5,6]
print(Solution.binary_search(test_array, 5))
print(Solution.binary_search(test_array, -1))
