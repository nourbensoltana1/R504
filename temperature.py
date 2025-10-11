def celsius_vers_fahrenheit(c):
    """Convertit Celsius → Fahrenheit"""
    return (c * 9/5) + 32


def fahrenheit_vers_celsius(f):
    """Convertit Fahrenheit → Celsius"""
    return (f - 32) * 5/9


def celsius_vers_kelvin(c):
    """Convertit Celsius → Kelvin"""
    return c + 273.15


def kelvin_vers_celsius(k):
    """Convertit Kelvin → Celsius"""
    return k - 273.15


def convertir_temperature():
    """Fonction principale de conversion de température"""
    print("\n--- Conversion de température ---")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")
    
    choix = input("Votre choix (1, 2, 3 ou 4) : ")
    
    try:
        valeur = float(input("Entrez la température à convertir : "))
        
        if choix == "1":
            resultat = celsius_vers_fahrenheit(valeur)
            print(f"{valeur}°C = {resultat:.2f}°F")
        elif choix == "2":
            resultat = fahrenheit_vers_celsius(valeur)
            print(f"{valeur}°F = {resultat:.2f}°C")
        elif choix == "3":
            resultat = celsius_vers_kelvin(valeur)
            print(f"{valeur}°C = {resultat:.2f}K")
        elif choix == "4":
            resultat = kelvin_vers_celsius(valeur)
            print(f"{valeur}K = {resultat:.2f}°C")
        else:
            print("❌ Choix invalide.")
    except ValueError:
        print("❌ Entrée invalide, veuillez saisir un nombre.")