from os.path import dirname, abspath, join
from re import findall
import matplotlib.pyplot as plot
import numpy as np

f = open(join(dirname(abspath(__file__)), "..", "data.txt"), "r")
text = f.read()

letters = {}
for letter in findall("[A-Za-z]", text):
  letter = letter.lower()
  if not letters.get(letter):
    letters[letter] = 1
  else:
    letters[letter] += 1
    
sortedLetters = []
for letter, n in letters.items():
  sortedLetters.append({ 'letter': letter, 'n': n })
sortedLetters = sorted(sortedLetters, key=lambda el: el.get('n'), reverse=True)
# for el in sortedLetters:
#   print(f"{el['letter'].upper()}: {el['n']} fois")

plot.hist([[v['letter']] * v['n'] for v in sortedLetters], bins=len(sortedLetters))
plot.show()