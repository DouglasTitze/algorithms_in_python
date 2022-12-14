# Function sorts array elements in place without making a new array
def sort_in_place(arr):

    # Iterate through 0 -> n-1
    for i in range(len(arr) - 1):

        # Create a variable that holds the index of the smallest value in the current iteratrion
        sml_idx = i

        # Iterate through i -> n
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[sml_idx]:
                sml_idx = j

        # Swap current index with that of the smallest index
        arr[i], arr[sml_idx] = arr[sml_idx], arr[i]

    return arr


print(sort_in_place([5, 3, 3, 1, 5, 56, 78, 8, 2, 2, 56, 7, 82, 100]))
