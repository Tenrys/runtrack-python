from os.path import dirname, abspath, join
from re import search, findall

f = open(join(dirname(abspath(__file__)), "..", "data.txt"), "r")
text = f.read()

c = 0
for word in findall("\w+", text):
  c += 1

print(f"Nombre de mots dans data.txt : {c}")
