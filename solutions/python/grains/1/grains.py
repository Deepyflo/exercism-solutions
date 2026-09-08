def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    result = 0
    for i in range(1, 65):
        result += square(i)
    return result