from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

#check if the name is ending with letter 'm'.
def check_mango_seller(name):
  return name[-1] == 'm'

def search_mango_seller(name):
  search_queue = deque()
  search_queue += graph["you"]
  searched = []
  while search_queue:
    person = search_queue.popleft()
    if not person in searched:
      if check_mango_seller(person):
        print(person + " is a mango seller!")
        return True
      else:
        search_queue += graph[person]
        searched.append(person)
  return False


if __name__ == "__main__":
  search_mango_seller("you")