import array
from unittest import result
from tabulate import tabulate


def add_rows_cols(table: array) -> None:
    """Formats the input table"""

    for i in range(0, len(table)):
        if not i:
            table[i][i] = "i/j"
        else:
            table[i][0] = f"{i}"

    for i in range(1, len(table[0])):
        table[0][i] = f"{i}"


def knapsack(max_capacity: int, weights: array, values: array) -> None:
    """Displays the knapsack problem for all possible items stolen"""

    num_items = len(values)
    table = [[0 for i in range(max_capacity + 1)] for _ in range(num_items + 1)]

    # For every item item in the house iterate
    for i in range(1, num_items + 1):
        # For every weight possible in the burglers bag
        for j in range(1, max_capacity + 1):
            if weights[i - 1] <= j:
                table[i][j] = max(
                    table[i - 1][j], values[i - 1] + table[i - 1][j - weights[i - 1]]
                )
            else:
                table[i][j] = table[i - 1][j]

    add_rows_cols(table)

    print("i (row) = max value, considering item i and the previous items")
    print("j (column) = Iterating all possible capacities of robber")
    print(f"{tabulate(table, tablefmt='pretty')}")


knapsack(6, [1, 3, 5, 6], [25, 30, 40, 35])
