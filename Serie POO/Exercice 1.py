class Joueur:

    def __init__(self, pseudo, identifiant, equipe):
        """ constructeur """
        self.pseudo = pseudo
        self.equipe = equipe
        self.id = identifiant
        self.nb_de_tirs_emis = 0
        self.liste_id_tirs_recus = []
        self.est_actif = True

    def tire(self):
        """méthode déclenchée par l'appui sur la gachette"""
        if self.est_actif == True:
            self.nb_de_tirs_emis = self.nb_de_tirs_emis + 1

    def est_determine(self):
        """methode qui renvoie True si le joueur réalise
        un  grand nombre de tirs"""
        return self.nb_de_tirs_emis > 500

    def subit_un_tir(self, id_recu):
        """méthode déclenchée par les capteurs de la
        veste"""
        if self.est_actif == True:
            self.est_actif = False
            self.liste_id_tirs_recus.append(id_recu)

    def redevenir_actif(self):
        if self.est_actif:
            return "Deja actif"
        else:
            self.est_actif == True

    def nb_de_tirs_recus(self):
        return len(self.liste_id_tirs_recus)




class Base:
    def __init__(self,equipe,liste_des_id_de_l_equipe):
        self.equipe = equipe
        self.liste_des_id_de_l_equipe = liste_des_id_de_l_equipe
        self.score = 1000

    def est_un_id_allie(self,id):
        return id in self.liste_des_id_de_l_equipe

    def incremente_score(self,inc):
        self.score +=inc

    def collecte_information(self, participant):
        if participant.equipe == self.equipe:  # test 1
            for id in participant.liste_id_tirs_recus:
                if self.est_un_id_allie(id):  # test 2
                    self.incremente_score(-20)
                else:
                    self.incremente_score(-10)
            if participant.est_determine():
                self.incremente_score(40)
                