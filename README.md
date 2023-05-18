# OpenClassrooms Projet7: Résolvez des problèmes en utilisant des algorithmes en Python

#
# AlgoInvest&Trade
#

#### Logo de l'entreprise
<img src="AlgoInvest&Trade.png">

#
Le problème est celui de déterminer la meilleure stratégie d'investissement pour un client avec un budget maximum de 500
euros, sachant qu'il ne peut acheter qu'une action à la fois, sans fractionner l'achat.

Nous pouvons décomposer le problème en plusieurs étapes :

1. Lecture des informations sur les actions à partir d'un fichier d'entrée.
2. Calculer le potentiel de gain pour chaque action en soustrayant son prix d'achat de sa valeur de vente projetée.
3. Trier les actions par ordre décroissant de potentiel de gain.
4. Sélectionner les actions dans l'ordre décroissant jusqu'à ce que le budget maximum soit atteint ou dépassé.
5. Retourner les actions sélectionnées.

Pour la première étape, nous aurions besoin de déterminer le format du fichier d'entrée. Par exemple, chaque ligne du
fichier pourrait contenir le nom de l'action, son prix d'achat et sa valeur de vente projetée, séparés par des virgules.

En ce qui concerne la solution de force brute, nous pourrions simplement parcourir toutes les combinaisons possibles
d'actions jusqu'à ce que nous atteignions le budget maximum. Cependant, cette approche serait très inefficace,
car le nombre de combinaisons possibles augmenterait de façon exponentielle à mesure que le nombre d'actions
augmenterait.

Une approche plus efficace consisterait à trier les actions par ordre décroissant de potentiel de gain et à les
sélectionner
dans cet ordre jusqu'à ce que le budget maximum soit atteint ou dépassé. Cette approche est plus efficace,
car elle ne nécessite pas de parcourir toutes les combinaisons possibles d'actions.

Pour l'algorithme optimisé, nous pourrions utiliser un algorithme de tri rapide pour trier les actions par ordre
décroissant de potentiel de gain, ce qui est efficace pour les grandes quantités de données. Nous pourrions ensuite
utiliser un algorithme glouton pour sélectionner les actions dans l'ordre trié jusqu'à ce que le budget maximum soit
atteint ou dépassé. Cela devrait donner une solution en temps raisonnable pour des ensembles de données de taille
raisonnable.

En comparant les résultats de l'algorithme optimisé avec ceux fournis par Sienna, nous pourrions examiner 
les différences dans les stratégies d'investissement proposées et analyser les raisons pour lesquelles 
elles diffèrent. Nous pourrions également comparer les performances de notre algorithme avec celles de Sienna 
pour évaluer l'efficacité de notre solution.

# Algorithme de notre solution
1. Lire les informations sur les actions à partir du fichier d'entrée
2. Calculer le potentiel de gain pour chaque action
3. Trier les actions par ordre décroissant de potentiel de gain
4. Sélectionner les actions dans l'ordre trié jusqu'à ce que le budget maximum soit atteint ou dépassé
5. Retourner les actions sélectionnées

### Code de force brutes

```python
import itertools


def investissement_force_brute(capacite, actions):
    nb_actions = len(actions)
    meilleures_actions = []
    meilleur_benefice = 0

    # Générer toutes les combinaisons possibles d'actions
    combinaisons = list(itertools.product([0, 1], repeat=nb_actions))

    # Parcourir toutes les combinaisons et trouver la meilleure stratégie
    for combinaison in combinaisons:
        total_achat = 0
        total_benefice = 0
        actions_selectionnees = []

        for i in range(nb_actions):
            if combinaison[i] == 1:
                action = actions[i]
                total_achat += action['prix_achat']
                if total_achat > capacite:
                    break
                total_benefice += action['benefice']
                actions_selectionnees.append(action)

        if total_benefice > meilleur_benefice:
            meilleur_benefice = total_benefice
            meilleures_actions = actions_selectionnees

    # Affichage des résultats
    print("Stratégie d'investissement optimale :")
    for action in meilleures_actions:
        print("- Action :", action['nom'], "Achat :", action['prix_achat'], "Vente :", action['prix_vente'])
    print("Bénéfice total :", meilleur_benefice)


# Exemple d'utilisation
capacite_totale = 50
liste_actions = [
    {'nom': 'Action 1', 'prix_achat': 10, 'prix_vente': 30, 'benefice': 0},
    {'nom': 'Action 2', 'prix_achat': 5, 'prix_vente': 20, 'benefice': 0},
    {'nom': 'Action 3', 'prix_achat': 12, 'prix_vente': 35, 'benefice': 0},
    {'nom': 'Action 4', 'prix_achat': 8, 'prix_vente': 25, 'benefice': 0},
    {'nom': 'Action 5', 'prix_achat': 15, 'prix_vente': 40, 'benefice': 0},
]

investissement_force_brute(capacite_totale, liste_actions)

````

#   

# Algorithme  d'optimisation

### 1. Lecture des données :

- Lire le fichier contenant les informations sur les actions.
- Chaque ligne du fichier représente une action avec son nom, son prix d'achat et son prix de vente.

### 2. Initialisation :

- Définir une variable pour représenter la capacité totale d'investissement.
- Définir une liste pour stocker les actions disponibles.

### 3. Calcul des bénéfices :

- Pour chaque action dans la liste des actions disponibles :
- Calculer le bénéfice en soustrayant le prix d'achat du prix de vente.
- Ajouter le bénéfice à l'action correspondante.
- Trier les actions par rapport au rapport bénéfice/prix d'achat de manière décroissante.

### 4. Sélection des actions :

- Initialiser une liste pour stocker les actions sélectionnées.
- Parcourir les actions triées et sélectionner les actions tant que la capacité totale n'est pas dépassée.
- Ajouter chaque action sélectionnée à la liste des actions sélectionnées.

### 5. Affichage des résultats :

Afficher la liste des actions sélectionnées, représentant la meilleure stratégie d'investissement.
Afficher le bénéfice total obtenu.

### Code d'optimisation

````python
def investissement_optimise(capacite, actions):
    nb_actions = len(actions)

    # Création de la matrice de programmation dynamique
    matrice = [[0] * (capacite + 1) for _ in range(nb_actions + 1)]

    # Remplissage de la matrice
    for i in range(1, nb_actions + 1):
        for j in range(1, capacite + 1):
            action_courante = actions[i - 1]
            if action_courante['prix_achat'] <= j:
                matrice[i][j] = max(
                    matrice[i - 1][j],
                    matrice[i - 1][j - action_courante['prix_achat']] + action_courante['benefice']
                )
            else:
                matrice[i][j] = matrice[i - 1][j]

    # Reconstruction de la solution optimale


total_benefice = matrice[nb_actions][capacite]
actions_selectionnees = []
i = nb_actions
j = capacite
while i > 0 and j > 0:
    if matrice[i][j] != matrice[i - 1][j]:
        action_selectionnee = actions[i - 1]
        actions_selectionnees.append(action_selectionnee)
        j -= action_selectionnee['prix_achat']
    i -= 1

# Affichage des résultats
print("Stratégie d'investissement optimale :")
for action in actions_selectionnees:
    print("- Action :", action['nom'], "Achat :", action['prix_achat'], "Vente :", action['prix_vente'])
print("Bénéfice total :", total_benefice)

# Exemple d'utilisation
capacite_totale = 50
liste_actions = [
    {'nom': 'Action 1', 'prix_achat': 10, 'prix_vente': 30, 'benefice': 0},
    {'nom': 'Action 2', 'prix_achat': 5, 'prix_vente': 20, 'benefice': 0},
    {'nom': 'Action 3', 'prix_achat': 12, 'prix_vente': 35, 'benefice': 0},
    {'nom': 'Action 4', 'prix_achat': 8, 'prix_vente': 25, 'benefice': 0},
    {'nom': 'Action 5', 'prix_achat': 15, 'prix_vente': 40, 'benefice': 0},
]

investissement_optimise(capacite_totale, liste_actions)
````

L'exécution de cet algorithme de programmation dynamique devrait être beaucoup plus rapide que l'utilisation d'une
approche de force brute. Cependant, la vitesse d'exécution dépend également de la taille des données et de la complexité
des calculs impliqués.

Il est important de noter que cet algorithme suppose que les actions peuvent être fractionnées, c'est-à-dire qu'il est
possible d'acheter une partie d'une action. Si cela n'est pas possible, vous devrez ajuster l'algorithme en conséquence.