from collections import Counter 

def find_first_non_repeated(string):
  char_counts = Counter(string)
  for char in string:
    if char in string:
      if char_counts[char] == 1:
        return char
    return char
  print(find_first_non_repeated("aabbccddeejffgghh"))
  #Output should be "j"