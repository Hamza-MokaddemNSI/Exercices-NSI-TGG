class Carte:
    def __init__(self,val,coul):
        self.valeur=val
        self.couleur=coul

def initialiser():
    jeu = []
    for c in ["coeur","carreau","trefle","pique"]:
        for v in range(2,15):
            carte_cree = Carte(v,c)
            jeu.append(carte_cree)
    return jeu

def comparer(carte1,carte2):
    if carte1.valeur == carte2.valeur:
        return 0
    elif carte1.valeur > carte2.valeur:
        return 1
    else:
        return -1


