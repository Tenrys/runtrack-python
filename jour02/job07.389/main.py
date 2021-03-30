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
      
  def setTitre(self, titre):
    self.__titre = titre
  def getTitre(self):
    return self.__titre
  
  def setAuteur(self, auteur):
    self.__auteur = auteur
  def getAuteur(self):
    return self.__auteur
    
  def print(self):
    print(self.__titre)

class Auteur(Personne):
  def __init__(self, prenom, nom):
    super().__init__(prenom, nom)
    self.__oeuvres = []

  def getOeuvres(self):
    return self.__oeuvres

  def listerOeuvres(self):
    print(f"Liste des oeuvres de {self.getPrenom()} {self.getNom()}:")
    for oeuvre in self.__oeuvres:
      print(oeuvre.getTitre())

  def ecrireUnLivre(self, titre):
    livre = Livre(titre, self)
    self.__oeuvres.append(livre)
    return livre
    
class Client(Personne):
  def __init__(self, prenom, nom):
    super().__init__(prenom, nom)
    self.__collection = []
    
  def getCollection(self):
    return self.__collection
    
  def inventaire(self):
    print(f"Collection de livres de {self.getPrenom()} {self.getNom()}:")
    for livre in self.__collection:
      print(f"Titre: {livre.getTitre()}")
    
class Bibliotheque:
  def __init__(self, nom):
    self.__nom = nom
    self.__catalogue = {}
    
  def setNom(self, nom):
    self.__nom = nom
  def getNom(self):
    return self.__nom
  
  def acheterLivre(self, auteur, titre, n=1):
    for livre in auteur.getOeuvres():
      if livre.getTitre().lower().strip() == titre.lower().strip():
        self.__catalogue[livre] = n
        return
  
  def inventaire(self):
    print(f"Catalogue de livres de la bibliothèque {self.__nom}:")
    for livre, n in self.__catalogue.items():
      print(f"Titre: {livre.getTitre()}, Quantité: {n}")

  def louer(self, client, titre):
    for livre, n in self.__catalogue.items():
      if livre.getTitre().lower().strip() == titre.lower().strip() and n > 0:
        client.getCollection().append(livre)
        self.__catalogue[livre] -= 1
        print(f"Le livre '{titre}' a été loué à {client.getPrenom()} {client.getNom()}")
        return
    print(f"Le livre '{titre}' n'est pas en stock")
        
  def rendreLivres(self, client):
    collection = client.getCollection()
    # Copy the collection so we can continue iterating over it while removing items in it
    for livre in list(collection): 
      try:
        self.__catalogue[livre] += 1
      except KeyError:
        self.__catalogue[livre] = 1
      collection.remove(livre)
    print(f"{client.getPrenom()} {client.getNom()} a rendu tous ses livres à la bibliothèque {self.getNom()}")
        
test = Auteur("David", "Ascher")
test.ecrireUnLivre("Learning Python")
test.ecrireUnLivre("Python Cookbook")

bibli = Bibliotheque("Pour Les Nuls")
bibli.acheterLivre(test, "Learning Python", 5)
bibli.acheterLivre(test, "Python Cookbook", 1)
bibli.inventaire()

client = Client("Marceau", "Maubert")
client.inventaire()
bibli.louer(client, "Learning Python")
bibli.louer(client, "Python Cookbook")
bibli.louer(client, "Python Cookbook")
bibli.inventaire()
client.inventaire()

bibli.rendreLivres(client)
bibli.inventaire()
client.inventaire()