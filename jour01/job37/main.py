import re

def next_word(word):
  word = list(word)
  word.reverse()
  for i, c in enumerate(word):
    nextChar = None
    try:
      nextChar = word[i + 1]
    except IndexError:
      pass
    if nextChar and c > nextChar:
      word[i], word[i + 1] = nextChar, c
      break
  word.reverse()
  return "".join(word)

word = None

try:
  word = input("Entrez un mot quelconque sans espaces, ni majuscules ou accents:\n")
  if re.search("[^a-z]", word): 
    raise Exception("Minuscules seulement")
except Exception as err:
  print(f"Mot invalide: {err}")
  exit()
  
print(next_word(word))
  