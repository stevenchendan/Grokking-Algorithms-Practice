phone_book = {}

def lookup(name):
  return phone_book[name]

def add_new(name, number):
  phone_book[name] = number

if __name__ == "__main__":
  add_new("steven", 449852021)
  print(lookup("steven"))