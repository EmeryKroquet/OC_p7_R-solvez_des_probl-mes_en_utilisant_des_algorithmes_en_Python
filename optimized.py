import itertools
from typing import List, Tuple


def optimize_pay(W: int, wt: List[int], val: List[int]) -> Tuple[int, List[int]]:
    """
    Dynamic programming approach to find the optimal solution to the 0/1 knapsack problem.
    Returns a tuple containing the maximum value and the list of items chosen.
    """
    n = len(val)
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i, w in itertools.product(range(1, n + 1), range(1, W + 1)):
        K[i][w] = (
            max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            if wt[i - 1] <= w
            else K[i - 1][w]
        )
    max_value = K[n][W]
    max_items = []
    w = W
    for i in range(n, 0, -1):
        if max_value <= 0:
            break
        if max_value == K[i - 1][w]:
            continue
        max_items.append(i - 1)
        max_value -= val[i - 1]
        w -= wt[i - 1]
    max_items.reverse()
    return K[n][W], max_items
