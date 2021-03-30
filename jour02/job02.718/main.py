class Personne:
  def __init__(self, prenom, nom):
    self.__prenom = prenom
    self.__nom = nom

  def SePresenter(self):
    print(f"Prénom: {self.getPrenom()}")
    print(f"Nom: {self.getNom()}")

  def setPrenom(self, prenom):
    self.__prenom = prenom

  def getPrenom(self):
    return self.__prenom

  def setNom(self, nom):
    self.__nom = nom

  def getNom(self):
    return self.__nom

class Livre:
  def __init__(self, titre, auteur):
    self.__titre = titre
    self.__auteur = auteur

  def print(self):
    print(self.__titre)
      
  def setTitre(self, titre):
    self.__titre = titre
  def getTitre(self):
    return self.__titre
  
  def setAuteur(self, auteur):
    self.__auteur = auteur
  def getAuteur(self):
    return self.__auteur

class Auteur(Personne):
  def __init__(self, prenom, nom):
    super().__init__(prenom, nom)
    self.__oeuvres = []

  def listerOeuvres(self):
    print(f"Liste des oeuvres de {self._Personne__prenom} {self._Personne__nom}:")
    for oeuvre in self.__oeuvres:
      print(oeuvre.getTitre())

  def ecrireUnLivre(self, titre):
    self.__oeuvres.append(Livre(titre, self))

test = Auteur("David", "Ascher")
test.ecrireUnLivre("Learning Python")
test.ecrireUnLivre("Python Cookbook")
test.listerOeuvres()
