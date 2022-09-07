import random


def binary_search(data, target):
    low = 0
    high = len(data) - 1
    mid = high // 2

    if not data:
        return "not in list"
    elif data[mid] == target or data[low] == target or data[high] == target:
        return "in list"
    elif data[mid] < target:
        return binary_search(data[mid + 1 : high], target)
    elif data[mid] > target:
        return binary_search(data[low:mid], target)


target = 8465
data = [
    1000,
    458,
    1558,
    8465,
    48965,
    561,
    849,
    5611,
    897,
    564,
    897,
    564,
    5644,
    89,
    645,
    5846,
    546,
    89,
    456,
    987,
    645,
    897,
    456,
    897,
    456,
    789,
    465,
    897,
]
data.sort()

print(binary_search(data, target))

print(list(enumerate(data)))
