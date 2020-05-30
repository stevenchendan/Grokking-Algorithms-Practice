def quick_sort(arr):
  if len(arr) < 2:
    return arr
  else:
    pivot = arr[0]
    less_than_pivot = [i for i in arr[1:] if i <= pivot]
    greater_than_pivot = [i for i in arr[1:] if i > pivot]
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)



if __name__ == "__main__":
  print(quick_sort([200, 100, 101, 20]))
