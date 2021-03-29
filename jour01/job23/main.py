
def draw_rectangle(width, height):
  str = ""
  for h in range(height):
    for w in range(width):
      if w == 0 or w == width - 1:
        str += "|"
      else:
        if h == 0 or h == height - 1:
          str += "-"
        else:
          str += " "
    str += "\n"
  print(str)

width, height = None, None

try:
  width = int(input("Entrez une largeur en chiffre:\n"), )
except:
  print("Veuillez entrer un chiffre pour la largeur")
  exit()
try: 
  height = int(input("Entrez une hauteur en chiffre:\n"))
except:
  print("Veuillez entrer un chiffre pour la hauteur")
  exit()

print("Voici votre rectangle:")
draw_rectangle(width, height)