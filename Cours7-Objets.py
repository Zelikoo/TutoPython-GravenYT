from model.cours7_player import Player
from model.cours7_weapon import Weapon

knife = Weapon("Couteau",3)

player1 = Player("ZelikO",20,3)
player1.damage(3)
print("Vous possedez désormais", player1.get_health(),"point de vie")

player2 = Player("BoB",20,5)

player1.attack_player(player2)
print(player1.get_pseudo(),"attaque",player2.get_pseudo())

print("Bienvenue au joueur", player1.get_pseudo(), "/ Points de vie:", player1.get_health(), "/ Attaque :", player1.get_attack_value())
print("Bienvenue au joueur", player2.get_pseudo(), "/ Points de vie:", player2.get_health(), "/ Attaque :", player2.get_attack_value())