from model.cours8_player import Player,Warrior
from model.Cours8_Batiment import Immeuble,Supermarche,Banque

warrior = Warrior("Darklord",30,4)
warrior.damage(4)
print("vie :",warrior.get_health(),"/ armure :",warrior.get_armor_point())

if issubclass(Warrior, Player):
    print("Le guerrier est bien une spécialisation de Player")

# Simulation de ville
# 4 immeubles
immeuble1 = Immeuble("26 rue de la Gravenade", 3, 3)
immeuble2 = Immeuble("28 rue de la Grevande", 5, 6)
immeuble3 = Immeuble("53 rue elios mitterand", 2, 2)
immeuble5 = Immeuble("120 rue pleiades", 8, 4)

# 2 supermarché
supermarche1 = Supermarche("27 rue de la Gravenade", 1, 12)
supermarche2 = Supermarche("119 rue pleiades", 4, 25)

# 1 banque
banque = Banque("53 rue elios mitterand", 25,20, "GravenBanque")