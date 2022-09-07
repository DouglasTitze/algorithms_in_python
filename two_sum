def two_sum(arr, target):

    """All permutations
    for i in range(len(arr)):
        for j in range(len(arr)):
            if (arr[i] + arr[j]) == target and i != j:
                print(i,j)
    """

    # All combinations
    return (
        (i, j)
        for i in range(len(arr))
        for j in range(i + 1, len(arr))
        if arr[i] + arr[j] == target
    )


print(list(two_sum([1, 2, 3], 4)))
