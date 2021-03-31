from os.path import dirname, abspath, join
from re import search, findall

length = None
try:
  length = int(input("Entrez un chiffre :\n"))
except ValueError:
  print("Valeur incorrecte")
  exit()

f = open(join(dirname(abspath(__file__)), "..", "data.txt"), "r")
text = f.read()

c = 0
for word in findall("\w+", text):
  if len(word) == length:
    c += 1

print(f"Nombre de mots de longueur {length} dans data.txt : {c}")
