
def welcome():
    print("Bienvenue")

def next_year():
    global year
    print("Fin de l'année ", year)
    year += 1
    print("Début de l'année ", year)

def addition(n=45):
    return 5+n

# creer une fonction max() qui va renvoyer le resultat le plus haut parmis 2 valeurs
def max(a,b):
    if a == b:
        return "Les deux nombres sont égaux"
    elif a > b:
        return a
    else:
        return b

# recursivité (fonction qui s'apelle elle même)
def add(a):
    a += 1
    print(a)

    if a < 10:
        add(a)


welcome()

year = 2020
next_year()

print("Le resultat du calcul est ",addition())
print("Le resultat du calcul est ",addition(7))

first_value = int(input("Entrer la premier valeur"))
second_value = int(input("Entrer la seconde valeur"))
print("La valeur max est ",max(first_value,second_value))

add(2)

# tp : une fonction pour calculer le nombre de voyelles dans un mot

# définir une fonction get_vowels_numbers(mot)
def get_vowels_numbers(mot):
    # créer un compteur de voyelles
    compteur = 0
    list_vowels = ["a","e","i","o","u","y"]
    # pour chaque lettre du mot vous verifiez s'il s'agit d'une voyelle
    for letter in mot:
        # si c'est le cas, on ajoute un au compteur
        if letter in list_vowels:
            compteur +=1
    # à la fin de la fonction, revoyer le compteur
    return compteur

mot_entree = input("Entrer un mot : ")
print("Le mot",mot_entree, "contient",get_vowels_numbers(mot_entree),"voyelles")