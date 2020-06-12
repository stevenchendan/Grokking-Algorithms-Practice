def find_station_conbination_cover_all_states(states_needed, stations):
  #handle edge case
  if states_needed == None or len(states_needed) == 0:
    return None
  final_stations = set()
  count = 0
  while states_needed:
    count += 1
    #if we cannot find perfact solution we will stop 
    #after iterate all the items in stations
    if count == len(stations):
      print ("There is no perfact solution for this states set. \
The follow stations is the best option we can find")
      break

    best_station = None
    states_covered = set()
    for station, states in stations.items():
      covered = states & states_needed
      if len(covered) > len(states_covered):
        best_station = station
        states_covered = covered
    
    states_needed -= states_covered
    final_stations.add(best_station)

  return final_stations




if __name__ == "__main__":
  #testing code
  states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
  states_needed_impossible = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az", "im"])
  stations = {}
  stations["kone"] = set(["id", "nv", "ut"])
  stations["ktwo"] = set(["wa", "id", "mt"])
  stations["kthree"] = set(["or", "nv", "ca"])
  stations["kfour"] = set(["nv", "ut"])
  stations["kfive"] = set(["ca", "az"])


  print (find_station_conbination_cover_all_states(states_needed, stations))
  print (find_station_conbination_cover_all_states(states_needed_impossible, stations))