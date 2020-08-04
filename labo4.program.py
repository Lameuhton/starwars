from starwars.force_users import ForceUsers, Jedi, Sith
from random import *

ORDRE_DEFAUT = 'Utilisateur'
NOM_DEFAUT = "Obi Wan Kenobi"
PDV_DEFAUT = 10
DAMAGE_DEFAUT = 5



def creer_combattant(ordre):

    #Crée un nom
    nom = input("Quel est le nom de votre combattant?: ")
    if nom == '':
        nom = NOM_DEFAUT

    #Crée des pdv
    pdv = input("Combien de point de vie a votre combattant?: ")
    if pdv == '':
        pdv = PDV_DEFAUT
    else:
        pdv = int(pdv)

    while pdv < 1:
        pdv = input("Veuillez entrer un nombre plus grand ou égal à 1: ")

    #Crée des dommages
    dommages = input("Combien de point de dommage à votre combattant?: ")

    if dommages == '':
        dommages = DAMAGE_DEFAUT
    else:
        dommages = int(dommages)
    while dommages < 1:
        dommages = input("Veuillez entrer un nombre plus grand ou égal à 1: ")


    #Vérifie de quel ordre vient le combattant pour créer l'objet de la classe correspondante
    if ordre == 1:
        combattant = ForceUsers(nom, pdv, dommages)
    elif ordre == 2:
        combattant = Jedi(nom, pdv, dommages)
    elif ordre == 3:
        combattant = Sith(nom, pdv, dommages)

    return combattant


def main():

    #Demande le nombre de combattant et le stock
    nb_combattants = int(input("Combien de combattants souhaitez-vous? (Minimum 2): "))
    combattants = []

    #Boucle pour créer la liste avec les combattants
    for i in range(1,nb_combattants+1):
        print(f"Combattant {i}")
        ordre = input("De quel ordre est votre combattant? (Utilisateur, Jedi ou Sith): ")
        if ordre != 'Utilisateur' and ordre != 'Jedi' and ordre != 'Sith':
            ordre = ORDRE_DEFAUT

        if ordre == "Utilisateur":
            combattants.append(creer_combattant(1))
        elif ordre == "Jedi":
            combattants.append(creer_combattant(2))
        elif ordre == "Sith":
            combattants.append(creer_combattant(3))

    #Tant qu'il reste au moins deux combattants vivants:
    print("------------Fight !------------")
    while len(combattants) >= 2:
        #Sélectionne aléatoirement deux combattants distincts
        player1, player2 = sample(combattants, 2)
        #Demande au premier d'utiliser la force sur le second
        print(player1.use_force_on(player2))
        print("_____________________________")
        #Vérifie si le second est toujours vivant, si non le retire de la liste des combattants
        if not player2.is_alive():
            combattants.remove(player2)

    #Affiche le nom du gagnant
    gagnant = combattants[0]
    print(f"Le gagnant est {gagnant.name} de l'ordre des {gagnant.__class__.__name__} avec {gagnant.HP} HP!")


if __name__ == '__main__':
    main()
