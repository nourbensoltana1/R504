def kilogramme_vers_livre(kg):
    """Convertit Kilogramme → Livre"""
    return kg * 2.20462


def livre_vers_kilogramme(lb):
    """Convertit Livre → Kilogramme"""
    return lb / 2.20462


def convertir_poids():
    """Fonction principale de conversion de poids"""
    print("\n--- Conversion de poids ---")
    print("1. Kilogramme → Livre")
    print("2. Livre → Kilogramme")
    
    choix = input("Votre choix (1, 2) : ")
    
    try:
        valeur = float(input("Entrez le poids à convertir : "))
        
        if choix == "1":
            resultat = kilogramme_vers_livre(valeur)
            print(f"{valeur}kg = {resultat:.2f}lb")
        elif choix == "2":
            resultat = livre_vers_kilogramme(valeur)
            print(f"{valeur}lb = {resultat:.2f}kg")
        else:
            print("❌ Choix invalide.")
    except ValueError:
        print("❌ Entrée invalide, veuillez saisir un nombre.")