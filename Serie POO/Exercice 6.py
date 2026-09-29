class Bim:
    def __init__(self,nature,surface,prix_moy):
        self.nt=nature
        self.sf=float(surface)
        self.pm=float(prix_moy)

    def estim_prix(self):
        mult=1
        if self.nt == 'maison':
            mult=1.1
        elif self.nt == 'bureau':
            mult=0.8
        return mult * (self.sf *  self.pm)

def nb_maison(lst):
    n=0
    for obj in lst:
        if obj.nt == 'maison':
            n+=1
    return n


b1 = Bim('maison',70,2000)
print(b1.estim_prix())  