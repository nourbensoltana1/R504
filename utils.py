def afficher_menu():
    print("\n==============================")
    print("      CONVERTISSEUR v2.0")
    print("==============================")
    print("1. Conversion de température")
    print("2. Conversion de distance")
    print("q. Quitter")
    print("==============================")

def demander_choix(choix_possibles):
    choix = input("Votre choix : ")
    if choix not in choix_possibles:
        print("Choix invalide")
        return demander_choix(choix_possibles)
    return choix

