def fibonacci(num):
    if num < 2:
        return num

    return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(7))