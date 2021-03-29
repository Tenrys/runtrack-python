from math import floor

def draw_triangle(height):
  width = height * 2
  str = ""
  for h in range(height):
    inTri = False
    for w in range(width):      
      if h == floor(width / 2) - 1 - w:
        str += "/"
        inTri = True
        continue
      if h == w - floor(width / 2):
        str += "\\"
        inTri = False
        continue
      if h == height - 1 and inTri:
        str += "_"
      else:
        str += " "
    str += "\n"
  print(str)

width, height = None, None

try: 
  height = int(input("Entrez une hauteur en chiffre:\n"))
except:
  print("Veuillez entrer un chiffre pour la hauteur")
  exit()

print("Voici votre triangle:")
draw_triangle(height)