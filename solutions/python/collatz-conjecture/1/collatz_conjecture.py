def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    result = number
    steps = 0
    while result != 1:
        if result % 2 == 0:
            result //= 2
        else:
            result = result * 3 + 1

        steps += 1

    return steps