"""
1. Lire les informations sur les actions à partir du fichier d'entrée
2. Générer toutes les combinaisons d'actions possibles
3. Pour chaque combinaison, calculer le potentiel de gain et vérifier si elle convient au budget max_value
4. Retourner la combinaison avec le potentiel de gain le plus élevé qui convient au budget max_value
"""

import csv
import time

# Création de tuples pour chaque action depuis fichier csv : nom de l'action, coût de l'action, % profit
with open("datas/dataset_force_brute.csv", mode="r") as file:
    reader = csv.reader(file)
    next(reader)
    data = [
        (row[0], float(row[1]), float(row[1]) * float(row[2]) / 100)
        for row in reader
    ]

# Jeu de données éventuel pour soutenance, avec 3 actions.
soutenance = [("action_1", 4, 6), ("action_2", 3, 5), ("action_3", 2, 4)]


# Fonction force brute, récursive, testant toutes les combinaisons possibles
def force_brute_algorithme(max_value, actions, actions_combinations=None):
    """
        Approche brute pour trouver la solution optimale au problème du sac à dos 0/1.
        Retourne un tuple contenant la valeur maximale et la liste des éléments choisis.
        """

    if actions_combinations is None:
        actions_combinations = []

    if not actions:
        return (
            sum(action[2] for action in actions_combinations),
            actions_combinations,
        )
    action = actions[0]
    profit_sans_action, liste_sans_action = force_brute_algorithme(max_value, actions[1:], actions_combinations)
    if action[1] <= max_value:
        profit_avec_action, liste_avec_action = \
            force_brute_algorithme(max_value - action[1], actions[1:], actions_combinations + [action])
        if profit_sans_action < profit_avec_action:
            return profit_avec_action, liste_avec_action
    return profit_sans_action, liste_sans_action


def main():
    start = time.perf_counter()
    result = force_brute_algorithme(500, data)
    stop = time.perf_counter()
    _extracted_from_main_5()
    for action in result[1]:
        print(action[0])
    _extracted_from_main_5()
    print(f"Profit max: {round(result[0], 2)}€")
    print(f"Somme dépensée: {sum(action[1] for action in result[1])}€")
    print(f"Temps de traitement: {round(stop - start, 2)}s")
    print("=============================================================")


# TODO Rename this here and in `main`
def _extracted_from_main_5():
    print("=============================================================\n"
          "=============================================================")
    print("Les résultats meilleurs actions sélectionnées:")
    print("=============================================================")


main()
