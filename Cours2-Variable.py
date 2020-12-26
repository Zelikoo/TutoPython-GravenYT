def main():
    # recolter une valeur porte monnaie
    wallet = int(input("Entrer le montant du porte monnaie: "))
    print("Vous avez actuellement", wallet, "euros")

    # creer un produit qui aura pour valeur 50
    priceproduct = 50
    print("Le Produit vaut ", priceproduct, "euros")

    # afficher la nouvelle valeur du porte monnaie, apres son achat
    wallet = wallet - priceproduct

    print("Produit acheté !")
    print("il reste " + str(wallet) + "€ dans le porte monnaie")


if __name__ == '__main__':
    main()