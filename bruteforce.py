"""
1. Lire les informations sur les actions à partir du fichier d'entrée
2. Générer toutes les combinaisons d'actions possibles
3. Pour chaque combinaison, calculer le potentiel de gain et vérifier si elle convient au budget max_value
4. Retourner la combinaison avec le potentiel de gain le plus élevé qui convient au budget max_value
"""

import csv
import time
from itertools import combinations


def find_best_combination(source, wallet):
    # Open the csv file with 'csv.DictReader'
    data = []
    with open(source, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        data.extend(iter(reader))

    # Declaration of variables useful for execution
    max_benefit = 0
    sum_cost_max_action = 0
    max_action = []

    all_comb = [list(combinations(data, n)) for n in range(len(data) + 1)]

    # Storage of each combination if cost is less than or equal to the wallet amount
    good_comb = []
    for comb in all_comb:
        for small_comb in comb:
            sum_cost = sum(int(element['price']) for element in small_comb)
            if sum_cost <= wallet:
                good_comb.append(small_comb)

    # Calculation of the 2-year profit for each combination and finding the best combination
    for comb in good_comb:
        sum_benefit = 0
        sum_cost = 0
        for action in comb:
            sum_benefit += int(action['price']) * (int(action['profit']) / 100)
            sum_cost += int(action['price'])
        if sum_benefit > max_benefit:
            max_benefit = sum_benefit
            max_action = comb
            sum_cost_max_action = sum_cost

    return max_action, sum_cost_max_action, max_benefit


def main():
    # Define fixed variables
    source = "datas/dataset_force_brute.csv"
    wallet = 500

    start_time = time.time()
    # Call the function and get the results
    best_combination, total_cost, total_profit = find_best_combination(source, wallet)
    end_time = time.time()

    print("=============================================================")
    print("Après analyse, Les meilleures combinaisons sont :")
    print("=============================================================")
    for action in best_combination:
        print(f" {action['name']}")
    print("=============================================================\n"
          "=============================================================")
    print("\nLe coût de cette combinaison est de {:0.2f}€".format(total_cost))
    print("Le bénéfice de cette combinaison est de {:0.2f}€ sur 2 ans".format(total_profit))
    execution_time = end_time - start_time
    print("Temps d'exécution : {:.4f} secondes".format(execution_time))
    print("=============================================================\n"
          "=============================================================")

if __name__ == "__main__":
    main()
