def countdown(number):
  print(number)
  if number <= 0:
    return 
  else:
    countdown(number-1)


if __name__ == "__main__":
  countdown(5)