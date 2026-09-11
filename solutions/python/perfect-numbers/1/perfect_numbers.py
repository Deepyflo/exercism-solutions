def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    if est_premier(number):
        return "deficient"

    aliquot_sum = 0

    for n in range(1, number):
        if number % n == 0:
            aliquot_sum += n

    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"

    
def est_premier(n):
    if n == 1:
        return False  # 1 n'est pas premier
    if n == 2:
        return True   # 2 est le seul nombre premier pair
    if n % 2 == 0:
        return False  # Exclure les autres nombres pairs
    
    # On teste les diviseurs impairs de 3 jusqu'à la racine carrée de n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
            
    return True