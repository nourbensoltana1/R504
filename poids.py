def kilogramme_vers_livre(kg):
    """Convertit Kilogramme → Livre"""
    return kg * 2.20462


def livre_vers_kilogramme(lb):
    """Convertit Livre → Kilogramme"""
    return lb / 2.20462


def kilogramme_vers_gramme(kg):
    """Convertit Kilogramme → Gramme"""
    return kg * 1000


def gramme_vers_kilogramme(g):
    """Convertit Gramme → Kilogramme"""
    return g / 1000


def kilogramme_vers_tonne(kg):
    """Convertit Kilogramme → Tonne"""
    return kg / 1000


def tonne_vers_kilogramme(t):
    """Convertit Tonne → Kilogramme"""
    return t * 1000


def convertir_poids():
    """Fonction principale de conversion de poids"""
    print("\n--- Conversion de poids ---")
    print("1. Kilogramme → Livre")
    print("2. Livre → Kilogramme")
    print("3. Kilogramme → Gramme")
    print("4. Gramme → Kilogramme")
    print("5. Kilogramme → Tonne")
    print("6. Tonne → Kilogramme")
    
    choix = input("Votre choix (1, 2, 3, 4, 5 ou 6) : ")
    
    try:
        valeur = float(input("Entrez le poids à convertir : "))
        
        if choix == "1":
            resultat = kilogramme_vers_livre(valeur)
            print(f"{valeur}kg = {resultat:.2f}lb")
        elif choix == "2":
            resultat = livre_vers_kilogramme(valeur)
            print(f"{valeur}lb = {resultat:.2f}kg")
        elif choix == "3":
            resultat = kilogramme_vers_gramme(valeur)
            print(f"{valeur}kg = {resultat:.2f}g")
        elif choix == "4":
            resultat = gramme_vers_kilogramme(valeur)
            print(f"{valeur}g = {resultat:.2f}kg")
        elif choix == "5":
            resultat = kilogramme_vers_tonne(valeur)
            print(f"{valeur}kg = {resultat:.2f}t")
        elif choix == "6":
            resultat = tonne_vers_kilogramme(valeur)
            print(f"{valeur}t = {resultat:.2f}kg")
        else:
            print("❌ Choix invalide.")
    except ValueError:
        print("❌ Entrée invalide, veuillez saisir un nombre.")