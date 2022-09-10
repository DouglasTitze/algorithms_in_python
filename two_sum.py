from array import array
import enum
from itertools import permutations


def two_sum(arr, target):

    # All permutations
    # for i in range(len(arr)):
    #    for j in range(len(arr)):
    #        if (arr[i] + arr[j]) == target and i != j:
    #            print(i,j)

    # All combinations
    return (
        (i, j)
        for i in range(len(arr))
        for j in range(i + 1, len(arr))
        if arr[i] + arr[j] == target
    )


def two_sum_hash_tables(arr: array, target: int) -> None:
    """This prints all the combinations of the two sum problem, but uses a hashtable to store old values that it has iterated through to make computation faster"""

    dic = {}

    for index, num in enumerate(arr):
        left_over = target - num

        if left_over in dic:
            print((index, dic[left_over]))

        else:
            dic[num] = index


print(list(two_sum([1, 2, 3], 4)))
two_sum_hash_tables([1, 2, 3], 4)
