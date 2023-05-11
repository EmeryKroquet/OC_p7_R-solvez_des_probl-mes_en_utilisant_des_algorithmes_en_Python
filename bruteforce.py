"""
1. Lire les informations sur les actions à partir du fichier d'entrée
2. Générer toutes les combinaisons d'actions possibles
3. Pour chaque combinaison, calculer le potentiel de gain et vérifier si elle convient au budget maximum
4. Retourner la combinaison avec le potentiel de gain le plus élevé qui convient au budget maximum
"""
import csv
import itertools

MAXIMUM_COST = 500


def read_csv_actions():
    actions = []
    csvfile = csv.DictReader(open('actions.csv'))
    for row in csvfile:
        action = (row['name'], int(row['price']), (int(row['profit']) * 0.01) * int(row['price']))
        actions.append(action)
    return actions


def investissement_actions_force_brute(actions, budget_max):
    # Générer toutes les combinaisons d'actions possibles
    combinaisons_actions = []
    for i in range(1, len(actions) + 1):
        combinaisons_actions += list(itertools.combinations(actions, i))

    # Calculer le potentiel de gain et vérifier si chaque combinaison convient au budget maximum
    meilleure_combinaison = None
    potentiel_gain_max = 0
    for combinaison in combinaisons_actions:
        prix_achat_total = sum(action['prix_achat'] for action in combinaison)
        if prix_achat_total <= budget_max:
            potentiel_gain = sum(
                action['valeur_vente'] - action['prix_achat']
                for action in combinaison
            )
            if potentiel_gain > potentiel_gain_max:
                potentiel_gain_max = potentiel_gain
                meilleure_combinaison = combinaison

    # Retourner la combinaison avec le potentiel de gain le plus élevé qui convient au budget maximum
    return list(meilleure_combinaison)
