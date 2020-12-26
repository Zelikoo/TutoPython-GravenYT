# 2 facons d'importer des modules
import statistics
from random import shuffle

# creer  une liste qui va stocker des pseudos pour simuler un jeu en ligne
online_players =["Zeliko", "Graven", "Mv", "Zerator", "Poki"]

# affiche la list
print(online_players)
# premier élément de la list
print(online_players[0])
# dernier élément de la list
print(online_players[len(online_players)-1])

# modif la list
online_players[1] = "Gravenito"
online_players[3:5] = ["Paul", "Jacque"]
print(online_players)

# Inserer dans la list
online_players.append("Gameur123")
online_players.extend(["Vald", "Lou"])
print(online_players)

# le joueur MV se deco
# del online_players(2)
# online_players.pop(2)
online_players.remove("Mv")
print(online_players)

# supprimer tous les elements de la liste
online_players.clear()
print(online_players)


####################
# exemple : jouer a la maitresse

notes = [
    8, 12, 10,
    15, 4, 20,
]

print(notes)
shuffle(notes)
print(notes)

# module statistic
result = statistics.mean(notes)
print("La moyenne de l'élève est de " + str(result))


####################
# notion de split
text = input("Entrer une chaine de la forme (email-pseudo-motdepasse)").split("-")
print(text)
print("Salut {}, ton email {}, ton mot de passe {}".format(text[1], text[0], text[2]))


######################
# generateur de phrase

# demander en console une chaine de la forme "mot1/mot2/mot3...
# transformer cette chaine en liste
listMot = input("Entrer une liste de mot sous la forme \"mot1/mot2/mot3...\"").split("/")

# la melanger
shuffle(listMot)
# si le nombre d'éléments de cette liste est inferieur à 10 -> afficher les deux premiers mots
if len(listMot) < 10:
    print(listMot[0], listMot[1])
else:
    # si le nombre d'élément est supérieur ou égal a 10 -> afficher les 3 derniers
    print(listMot[len(listMot) - 3], listMot[len(listMot) - 2], listMot[len(listMot) - 1])
