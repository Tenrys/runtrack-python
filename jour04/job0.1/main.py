def factorielle(n, v=None):
  if not v:
    v = n
  if n > 1:
    n -= 1
    return factorielle(n, v * n)
  else:
    return v
    
try:
  val = int(input("Entrez un nombre entier : "))
  if isinstance(val, float):
    print("Valeur invalide")
    exit()
except ValueError:
  print("Valeur invalide")
  exit()

print(f"Factorielle de {val}:")
print(factorielle(val))