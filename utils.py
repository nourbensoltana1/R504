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

def confirmer_recommencer():
    reponse = input("\nSouhaitez-vous faire une autre conversion ? (o/n) : ").lower()
    while reponse not in ["o", "n"]:
        print("Veuillez répondre par 'o' pour oui ou 'n' pour non.")
        reponse = input("Souhaitez-vous faire une autre conversion ? (o/n) : ").lower()
    return reponse == "o"


