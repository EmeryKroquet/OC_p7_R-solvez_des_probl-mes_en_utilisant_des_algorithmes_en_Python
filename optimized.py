import csv
import itertools
import time

def read_data_from_csv(csv_file):
    """
    Lit les données du fichier CSV et retourne une liste de tuples contenant les informations sur les actions.
    """
    data = []
    with open(csv_file, mode="r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            cost = int(float(row[1]) * 100)
            if cost > 0:
                name = row[0]
                profit = float(row[1]) * float(row[2])
                data.append((name, cost, profit))

    return data


def optimized_algorithm(max_value, actions):
    """
    Algorithme optimisé utilisant une approche de programmation dynamique pour trouver la solution optimale
    au problème du sac à dos 0/1.
    Renvoie un tuple contenant la valeur maximale et la liste des éléments choisis.
    """
    matrix = [[0 for _ in range(max_value + 1)] for _ in range(len(actions) + 1)]

    for y, x in itertools.product(range(1, len(actions) + 1), range(1, max_value + 1)):
        matrix[y][x] = (
            max(
                actions[y - 1][2] + matrix[y - 1][x - actions[y - 1][1]],
                matrix[y - 1][x],
            )
            if actions[y - 1][1] <= x
            else matrix[y - 1][x]
        )

    n = len(actions)
    actions_combinations = []

    while max_value >= 0 and n >= 0:
        action = actions[n - 1]
        if matrix[n][max_value] == matrix[n - 1][max_value - action[1]] + action[2]:
            actions_combinations.append(action)
            max_value -= action[1]
        n -= 1

    return matrix[-1][-1], actions_combinations


def main():
    csv_file = "datas/dataset_force_brute.csv"
    max_value = 50000

    start = time.perf_counter()
    actions = read_data_from_csv(csv_file)
    result = optimized_algorithm(max_value, actions)
    stop = time.perf_counter()

    print("=============================================================")
    print("Les meilleures combinaisons sont :")
    print("=============================================================")
    for action in result[1]:
        print(action[0])
    print("=============================================================")
    print(f"Le coût de la combinaison est de : {sum(action[1] / 100 for action in result[1])}€")
    print(f"Le bénéfice de la combinaison est de : {round(result[0] / 100, 2)}€ sur 2 ans")
    print(f"Temps de traitement : {round(stop - start, 2)}s")
    print("=============================================================")


if __name__ == "__main__":
    main()
