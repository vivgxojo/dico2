def simuler_attaque(j1: dict, j2: dict):
    """
    Simuler une attanque entre 2 joueurs
    :param j1: dictionnaire de stats du joueur 1
    :param j2: dictionnaire de stats du joueur 2
    """
    dict_stats_j1["PV"] -= dict_stats_j2["Attaque"]
    dict_stats_j2["PV"] -= dict_stats_j1["Attaque"]

dict_stats_j1 = {   # TODO : ajouter la défense
    "Attaque" : 5,
    "PV" : 100
}
dict_stats_j2 = {
    "Attaque" : 3,
    "PV" : 100
}
# TODO : faire un boucle pour plusieurs attaques avec des valeurs aléatoires
dict_stats_j3 = dict_stats_j1 # pas une copie, ça reste le même dictionnaire
dict_stats_j4 = dict_stats_j2.copy() # copie : créer un nouveau dictionnaire et copier les valeurs
print(dict_stats_j1, dict_stats_j2)
simuler_attaque(dict_stats_j1, dict_stats_j2)
print(dict_stats_j1, dict_stats_j2)
print(dict_stats_j3) # oups le j3 a été attaqué en même temps que le j1 car c'est le même joueur
print(dict_stats_j4)