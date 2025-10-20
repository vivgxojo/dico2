def simuler_attaque(j1: dict, j2: dict):
    """
    Simuler une attanque entre 2 joueurs
    :param j1: dictionnaire de stats du joueur 1
    :param j2: dictionnaire de stats du joueur 2
    :return: j1, j2 : tuples des dictionnaires des 2 joueurs
    """
    # TODO : prendre en compte la défense
    j1["PV"] -= j2["Attaque"]    # si (attaque - défense) > 0
    j2["PV"] -= j1["Attaque"]    # pv = pv - (attaque - défense)
    return j1, j2

dict_stats_j1 = {
    "Attaque" : 5,
    "Defense" : 3,
    "PV" : 100
}
dict_stats_j2 = {
    "Attaque" : 3,
    "Defense" : 7,
    "PV" : 100
}
# TODO : faire un boucle pour plusieurs attaques avec des valeurs aléatoires
# boucle infinie
    # générer attaque aléatoire pour chaque joueur
    # mettres le valeurs d'attanques dans les dictionnaires
    # appeler la fonction
    # afficher l'état du jeu
    # si un joueur 0 PV ou moins, terminer

# Test - notes de cours
dict_stats_j3 = dict_stats_j1 # pas une copie, ça reste le même dictionnaire
dict_stats_j4 = dict_stats_j2.copy() # copie : créer un nouveau dictionnaire et copier les valeurs
print(dict_stats_j1, dict_stats_j2)
dict_stats_j1, dict_stats_j2 = simuler_attaque(dict_stats_j1, dict_stats_j2)
print(dict_stats_j1, dict_stats_j2)
print(dict_stats_j3) # oups le j3 a été attaqué en même temps que le j1 car c'est le même joueur
print(dict_stats_j4)