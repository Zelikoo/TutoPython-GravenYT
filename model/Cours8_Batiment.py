
class Batiment:
    def __init__(self,adresse,nb_etages):
        self.adresse = adresse
        self.nb_etage = nb_etages

    def get_adresse(self):
        return self.adresse

    def get_nb_etage(self):
        return self.nb_etage


class Immeuble(Batiment):
    def __init__(self,adresse,nb_etage,nb_balcons):
        super().__init__(adresse,nb_etage)
        self.nb_balcon = nb_balcons

    def get_nb_balcon(self):
        return self.nb_balcon


class Supermarche(Batiment):
    def __init__(self,adresse,nb_etage,nb_rayons):
        super().__init__(adresse,nb_etage)
        self.nb_rayons = nb_rayons

    def get_nb_rayons(self):
        return self.nb_rayons


class Banque(Batiment):
    def __init__(self,adresse,nb_etage,nb_coffres,nom):
        super().__init__(adresse,nb_etage)
        self.nb_coffres = nb_coffres
        self.nom = nom

    def get_nb_coffres(self):
        return self.nb_coffres

    def get_nom(self):
        return self.nom