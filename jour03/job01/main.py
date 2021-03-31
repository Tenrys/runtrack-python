from os.path import dirname, abspath

f = open(dirname(abspath(__file__)) + "/output.txt", "r")
print(f.read())
f.close()