# OC_p7_R-solvez_des_probl-mes_en_utilisant_des_algorithmes_en_Python

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
car le nombre de combinaisons possibles augmenterait de façon exponentielle à mesure que le nombre d'actions augmenterait.

Une approche plus efficace consisterait à trier les actions par ordre décroissant de potentiel de gain et à les sélectionner 
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

# Algorithme de force brutes

def investissement_actions(actions, budget_max):
    # Calculer le potentiel de gain pour chaque action
    for action in actions:
        action['potentiel_gain'] = action['valeur_vente'] - action['prix_achat']
    
    # Trier les actions par ordre décroissant de potentiel de gain
    actions_triees = sorted(actions, key=lambda k: k['potentiel_gain'], reverse=True)
    
    # Sélectionner les actions dans l'ordre trié jusqu'à ce que le budget maximum soit atteint ou dépassé
    budget_utilise = 0
    actions_selectionnees = []
    for action in actions_triees:
        if budget_utilise + action['prix_achat'] <= budget_max:
            budget_utilise += action['prix_achat']
            actions_selectionnees.append(action)
    
    # Retourner les actions sélectionnées
    return actions_selectionnees
