def quick_sort(arr):
    arr_len = len(arr)

    if arr_len == 0 or arr_len == 1:
        return arr

    mid = arr_len // 2

    left = filter(lambda x: x < arr[mid], arr)
    right = filter(lambda x: x > arr[mid], arr)
    center = filter(lambda x: x == arr[mid], arr)

    return quick_sort(list(left)) + list(center) + quick_sort(list(right))


print(quick_sort([1, 1, 2, 4, 5, 6, 7]))
