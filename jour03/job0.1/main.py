from os.path import dirname, abspath

f = open(dirname(abspath(__file__)) + "/output.txt", "w")
f.write(input("Entrez une chaîne de caractères :\n"))
f.close()
print("Ecrit dans output.txt")
