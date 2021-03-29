numbers = []

for i in range(5):
  numbers.append(input(f"Entrez le chiffre numéro {i + 1}\n"))
  
numbers.sort()

print("Voici vos chiffres par ordre croissant :")
for n in numbers:
  print(n)
