# Convertisseur d'unités (Python)

Petit projet en binôme pour découvrir **Git**, **GitHub** et la **collaboration** sur un dépôt partagé.

## Objectif

Créer un programme en Python capable de convertir :
- des **températures** (Celsius ↔ Fahrenheit)
- des **distances** (mètres ↔ kilomètres)

Le projet est découpé en **plusieurs fichiers** pour permettre un vrai travail collaboratif.

---

## Structure du projet
convertisseur/
│
├── main.py # point d'entrée du programme (menu principal)
├── temperature.py # conversions de température
├── distance.py # conversions de distance
└── utils.py # fonctions d'affichage et de validation

---

## Organisation du travail

| Rôle | Tâches principales | Fichiers concernés |
|------|--------------------|--------------------|
| **Chef de projet** | Crée le dépôt GitHub, initialise le projet, code le menu principal et les conversions de température. | `main.py`, `temperature.py` |
| **Collaborateur** | Clone le dépôt, ajoute les conversions de distance et les fonctions utilitaires. | `distance.py`, `utils.py` |

---

## Installation

1. **Cloner le dépôt**  
   ```bash
   git clone git@github.com:TonNomUtilisateur/convertisseur.git
   cd convertisseur

Exécuter le programme
python3 main.py
Exemple d’exécution

=== Convertisseur d'unités ===

--- MENU PRINCIPAL ---
1. Conversion de température
2. Conversion de distance
q. Quitter
Votre choix : 1

--- Conversion de température ---
1. Celsius → Fahrenheit
2. Fahrenheit → Celsius
Votre choix (1 ou 2) : 1
Entrez la température à convertir : 25
25.0 °C = 77.00 °F

Technologies utilisées
Python 3.x


Git / GitHub
Auteurs
Chef de projet : nour bensoltana
Collaborateur : Ons Ammar
Projet réalisé dans le cadre d’un exercice sur le versioning et la collaboration Git.
