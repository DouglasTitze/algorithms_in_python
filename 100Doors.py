# Create doors
doors = [False] * 101

# Iterate 1 -> 100
for num_doors in range(1, 101):

    # Iterate from num_doors -> 100 taking steps at a rate of num_doors
    for i in range(num_doors, 101, num_doors):

        # Flip the doors status
        doors[i] = not doors[i]


# Print all the doors that are open (True)
print(list(i for i in range(1, 101) if doors[i]))

"""The code above is equal to the following block
for i in range(1,101):
    if doors[i]:
        print(i)
"""
