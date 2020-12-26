from random import randint

for num_client in range(1,6):
    print("Vous etes le client n°", num_client)

emails = ["dcyril95@gmail.com", "cduval@live.fr", "test@gmail.com", "senseii95@hotmail.fr"]
blacklist = ["test@gmail.com","test@gmail.com"]


for email in emails:
    if email in blacklist:
        print("Email " + email + " interdit ! Envoi impossible")
        continue

    print("Email envoyé à: ", email)


# while : tant qu'une condition est vrai
# salarie 1500€ / mois
salary = 1500

# tant que salaire < 2000€, + 120€
while salary <2000:
    salary +=120
    print("Votre salaire actuel est de ", salary,"€")

print("Fin du programme")

# Jeu du juste Prix
# choisir un nombre entre 1 et 1000
nombreCherche = randint(1,100)
# tant que le jeu n'est pas fini
nb = 0
while int(nombreCherche) != int(nb):
    #   -> demander un nouveau prix
    nb = input("prix : ")
    #   -> si il trouve "C'est gagné"
    if int(nombreCherche) == int(nb):
        print("C'est gagné !")
    else:
        #   -> sinon on affiche "C'est moins" ou "C'est plus"
        if int(nombreCherche) < int(nb):
            print("C'est moins")
        else:
            print("C'est plus")

