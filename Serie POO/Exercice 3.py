class Stock:
    def __init__ (self):
        self.qt_farine = 0 # quantité de farine initialisée à 0 g
        self.nb_oeufs = 0 # nombre d’œufs (0 à l’initialisation)
        self.qt_beurre = 0 # quantité de beurre initialisée à 0 g

    def ajouter_beurre(self,qt):
        self.qt_beurre+= qt

    def ajouter_farine(self,qt):
        self.qt_farine+= qt

    def ajouter_oeufs(self,nb):
            self.nb_oeufs+= nb

    def afficher(self):
        print(f"\nfarine: {self.qt_farine}\noeuf: {self.nb_oeufs}\nbeurre: {self.qt_beurre}")

    def stock_suffisant_brioche(self):
        return self.qt_farine >= 350 and self.nb_oeufs >=4 and self.qt_beurre >= 175

    def produire(self):
        res = 0
        while self.stock_suffisant_brioche():
            self.qt_beurre = self.qt_beurre - 175
            self.qt_farine = self.qt_farine - 350
            self.nb_oeufs = self.nb_oeufs - 4
            res = res + 1
        return res


mon_stock=Stock()
mon_stock.ajouter_beurre(1000)
mon_stock.ajouter_farine(1000)
mon_stock.ajouter_oeufs(10)
print(mon_stock.produire())
mon_stock.afficher()


def nb_brioches(liste_stocks):
    n=0
    for stock in liste_stocks:
        n+=stock.produire()
    return n