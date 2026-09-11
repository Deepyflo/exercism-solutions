def score(x, y):
    max_radius = 10
    middle_radius = 5
    min_radius = 1
    
    distance = (x ** 2 + y ** 2) ** .5

    if distance <= min_radius:
        return 10
    elif distance <= middle_radius:
        return 5
    elif distance <= max_radius:
        return 1
    else:
        return 0