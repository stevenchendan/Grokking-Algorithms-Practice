# Finds the smallest value in an array
def find_smallest_item_index(array):
  smallest = array[0]
  smallest_Index = 0
  for i in range(1, len(array)):
    if array[i] < smallest:
      smallest = array[i]
      smallest_Index = i

  return smallest_Index



def selection_sort(array):
  result = []
  for i in range(len(array)):
    smallest = find_smallest_item_index(array)
    result.append(array.pop(smallest))
  return result


#test
test_array = [3,2,3,1,5,6]
print(selection_sort(test_array))
