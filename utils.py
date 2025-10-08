def afficher_menu():
    print("1. Convertir une température")
    print("2. Convertir une distance")
    print("q. Quitter")

def demander_choix(choix_possibles):
    choix = input("Votre choix : ")
    if choix not in choix_possibles:
        print("Choix invalide")
        return demander_choix(choix_possibles)
    return choix

