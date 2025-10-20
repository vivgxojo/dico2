import pytest
from dico2 import simuler_attaque
#TODO : Corriger le test pour prendre en compte la défense
#TODO : Ajouter d'autres tests
def test_dict_stats_j2():
    #arrange
    dict_stats_j1 = {
        "Attaque": 5,
        "PV": 100
    }
    dict_stats_j2 = {
        "Attaque": 3,
        "PV": 100
    }
    pv_j1_att = 97
    pv_j2_att = 95
    #act
    dict_j1, dict_j2 = simuler_attaque(dict_stats_j1, dict_stats_j2)
    #assert
    assert dict_j1["PV"] == pv_j1_att
    assert dict_j2["PV"] == pv_j2_att