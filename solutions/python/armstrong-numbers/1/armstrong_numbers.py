def is_armstrong_number(number):
    result = 0
    number_length = len(str(number))
    
    for num in str(number):
        result += int(num) ** number_length

    return result == number