voted = {}

def check_existing_voter(name):
  if voted.get(name):
    print("kick him out")
  else:
    voted[name] = True
    print("let him vote")

if __name__ == "__main__":
  voted["steven"] = True
  check_existing_voter("steven")
  check_existing_voter("chen")