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
    
test = Personne("Marceau", "Maubert")
test.SePresenter()

test.setPrenom("John")
test.setNom("Doe")
test.SePresenter()