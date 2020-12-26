
# exemple : Systeme de verification de mot de passe
password = input("Entrer votre mot de passe")

# verification si le mot de passe est inferieur à 8 caractères
if len(password) <=8:
    print("Mot de passe trop court !")
elif 8 < len(password) <= 12:
    print("Mot de passe moyen !")
else:
    print("Mot de passe parfait !")

print(len(password))

# Place de cinema
# recolter l'age de la personne
age = int(input("Quel est votre age ? "))
print("Vous avez " + str(age) + " ans")

# si la personne est mineur -> 7€
if age < 18:
    montant = 7
# si majeur -> 12€
elif age >= 18:
    montant = 12

#souhaitez-vous du pop-corn
popcorn = input("Souhaitez-vous du pop-Corn? ")

if popcorn.upper() == "OUI":
    montant += 5

print("Le montant est de " + str(montant) + "€")
