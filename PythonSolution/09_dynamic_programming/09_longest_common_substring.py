#pesudo code
def common_substring_length(word_a: str, word_b: str) -> int:
  cell = [[0 for x in range(len(word_a))] for y in range(len(word_b)]
  for i in range(len(word_a)):
    for j in range(len(word_b)):
      if word_a[i] == word_b[j] and i * j != 0:
        cell[i][j] = cell[i-1][y-1] + 1
      elif: word_a[i] == word_b[j] and i * j == 0:
        cell[i][j] = 1
      else:
        cell[i][j] = 0
  return cell[i][j]

def longest_common_substring(potential_words: List[str], user_input_word: str) -> str:
  #handle edge case
  if potential_words == None or len(potential_words) == 0:
    return ""
  
  longest_word = potential_words[0]
  max_length = 0
  for item in potential_words:
    length = common_substring_length(item, user_input_word)
    if length > max_length:
      longest_word = item
  return longest_word