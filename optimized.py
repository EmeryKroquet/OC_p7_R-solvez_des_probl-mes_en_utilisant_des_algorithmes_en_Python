import csv
import itertools
import time

csv_file = "datas/dataset2_Python+P7.csv"

# Création de tuples pour chaque action depuis fichier csv_file: nom de l'action, coût de l'action, % profit
with open(csv_file, mode="r") as file:
    reader = csv.reader(file)
    next(reader)

    data = [
        (row[0], int(float(row[1]) * 100), float(row[1]) * float(row[2]))
        for row in reader
        if float(row[1]) > 0
    ]


# Algorithme dynamique
def algorithme_optimised(max_value, actions):
    """
        Approche de programmation dynamique pour trouver la solution optimale au problème du sac à dos 0/1.
        Renvoie un tuple contenant la valeur maximale et la liste des éléments choisis.
        """

    matrix = [[0 for _ in range(max_value + 1)] for _ in range(len(actions) + 1)]

    # axe-y pour la liste des actions
    for y, x in itertools.product(range(1, len(actions) + 1), range(1, max_value + 1)):
        # si le coût de l'action > montant
        matrix[y][x] = (
            max(
                actions[y - 1][2] + matrix[y - 1][x - actions[y - 1][1]],
                matrix[y - 1][x],
            )
            if actions[y - 1][1] <= x
            else matrix[y - 1][x]
        )
    # Retrouver les actions sélections en balayant la matrix en sens inverse
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
    start = time.perf_counter()
    result = algorithme_optimised(48924, data)
    stop = time.perf_counter()
    extracted_from_main()
    for action in result[1]:
        print("\n", action[0])
    extracted_from_main()
    print(f"Profit maximal: {round(result[0] / 100, 2)}€")
    print(f"Somme dépensée: {sum(action[1] / 100 for action in result[1])}€")
    print(f"Temps de traitement: {round(stop - start, 2)}s")
    print("=============================================================")


# TODO Rename this here and in `main`
def extracted_from_main():
    print("=============================================================\n"
          "=============================================================")
    print("Les meilleurs résultats des actions sélectionnées: ")
    print("=============================================================")


if __name__ == "__main__":
    main()
