from utils import afficher_menu, demander_choix, confirmer_recommencer, afficher_aide
from temperature import convertir_temperature
from distance import convertir_distance


def main():
    print("Bienvenue dans notre convertisseur d’unités développé en binôme !")

    while True:
        afficher_menu()
        choix = demander_choix(["1", "2", "h", "q"])

        if choix == "1":
            convertir_temperature()
        elif choix == "2":
            convertir_distance()
        elif choix == "h":
            afficher_aide()
        elif choix == "q":
            print("Merci d’avoir utilisé le convertisseur !")
            break

        # Confirmation de redémarrage
        if not confirmer_recommencer():
            print("Merci d’avoir utilisé le convertisseur !")
            break


if __name__ == "__main__":
    main()
