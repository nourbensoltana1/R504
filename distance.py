def metres_vers_kilometres(m):
    """Convertit mètres → kilomètres"""
    return m / 1000


def kilometres_vers_metres(km):
    """Convertit kilomètres → mètres"""
    return km * 1000


def convertir_distance():
    print("\n--- Conversion de distance ---")
    print("1. Mètres → Kilomètres")
    print("2. Kilomètres → Mètres")

    choix = input("Votre choix (1 ou 2) : ")

    try:
        valeur = float(input("Entrez la distance à convertir : "))
    except ValueError:
        print("Entrée invalide, veuillez saisir un nombre.")
        return

    if choix == "1":
        resultat = metres_vers_kilometres(valeur)
        print(f"{valeur} m = {resultat:.3f} km")
    elif choix == "2":
        resultat = kilometres_vers_metres(valeur)
        print(f"{valeur} km = {resultat:.0f} m")
    else:
        print("Choix invalide.")
