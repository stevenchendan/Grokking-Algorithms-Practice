def countdown(number):
  print(number)
  if number <= 0:
    return 
  else:
    countdown(number-1)

countdown(5)