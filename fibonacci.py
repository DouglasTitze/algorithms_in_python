def fibonacci(num):
    if num < 2:
        return num

    return fibonacci(num - 1) + fibonacci(num - 2)


def fib_cache(num: int, cache=None) -> int:
    """Computes fibonacci sequence and caches values to avoid repetition"""
    if cache is None:
        cache = {}

    if num in cache.keys():
        return cache[num]

    if num < 2:
        cache[num] = 1
        return 1

    result = fib_cache(num - 1, cache) + fib_cache(num - 2, cache)
    cache[num] = result
    return result


# Takes 29 seconds
# print(fibonacci(40))

# Takes 0.062 seconds
print(fib_cache(40))
