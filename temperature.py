def celsius_vers_fahrenheit(c):
	"""Convertit Celsius → Fahrenheit"""
	return (c * 9/5) + 32

def fahrenheit_vers_celsius(f):
	"""Convertit Fahrenheit → Celsius"""
	return (f - 32) * 5/9
def convertir_temperature():
	print("\n--- Conversion de température ---")
	print("1. Celsius → Fahrenheit")
	print("2. Fahrenheit → Celsius")

	choix = input("Votre choix (1 ou 2) : ")

	try:
    	valeur = float(input("Entrez la température à convertir : "))
	except ValueError:
    	print("Entrée invalide, veuillez saisir un nombre.")
    	return

	if choix == "1":
    	resultat = celsius_vers_fahrenheit(valeur)
    	print(f"{valeur} °C = {resultat:.2f} °F")
	elif choix == "2":
    	resultat = fahrenheit_vers_celsius(valeur)
    	print(f"{valeur} °F = {resultat:.2f} °C")
	else:
    	print("Choix invalide.")
