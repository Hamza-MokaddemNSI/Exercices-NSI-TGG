from random import randint
from math import *

Mousse = [None, None, None,None, None, None]

class Cbulle:
    def __init__(self):
        self.xc = randint(0, 100)
        self.yc = randint(0, 100)
        self.rayon = randint(0, 10)
        self.dirx = float(randint(-1, 1)) # dirx et diry valent
        self.diry = float(randint(-1, 1)) # -1.0 ou 0.0. ou 1.0
        self.couleur = randint(1,65535)

    def bouge(self):
        # déplace la bulle
        self.xc = self.xc + self.dirx
        self.yc = self.yc + self.diry

def donnePremierIndiceLibre(Mousse):
    """Mousse est une liste.
    La fonction doit renvoyer l indice du premier
    emplacement libre (contenant None) dans la liste Mousse
    ou renvoyer 6 en l absence d un emplacement libre dans
    Mousse."""

    i = 0
    while i<= len(Mousse) and Mousse[i] != None :
        i+=1
    return i

def placeBulle(B):
    for i in range(len(Mousse)):
        if Mousse[i] == None:
            Mousse[i] == B

def distanceEntreBulles(B1,B2):
    return sqrt(pow(B2.xc - B1.xc ,2) + pow(B2.yc - B1.yc,2))

def bullesEnContact(B1, B2):
    return B1.rayon + B2.rayon >= distanceEntreBulles(B1,B2)

def collision(indPetite, indGrosse, mousse) :
    """
    Absorption de la plus petite bulle d indice indPetite
    par la plus grosse bulle d indice indGrosse. Aucun test
    n est réalisé sur les positions.
    """
    # calcul du nouveau rayon de la grosse bulle
    surfPetite = pi*Mousse [indPetite].rayon**2
    surfGrosse = pi*Mousse [indGrosse].rayon**2
    surfGrosseApresCollision = surfGrosse + surfPetite
    rayonGrosseApresCollision = sqrt(surfGrosseApresCollision/pi)
    #réduction de 50% de la vitesse de la grosse bulle
    Mousse[indGrosse].dirx = Mousse[indGrosse].dirx/2
    Mousse[indGrosse].diry = Mousse[indGrosse].diry/2
    #suppression de la petite bulle dans Mousse
    Mousse[indPetite] = None
    Mousse[indGrosse].rayon = rayonGrosseApresCollision # car l affecte pas