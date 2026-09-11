def is_valid(isbn):
    only_digit = isbn.replace('-', '')

    digits = []

    for idx, number in enumerate(only_digit):
        if number == "X" and idx < len(only_digit) - 1:
            return False
        elif number == "X":
            number = 10
        elif not number.isdigit():
            return False
        else:
            number = int(number)
                
        digits.append(number) 

    if len(digits) != 10:
        return False
        
    return (digits[0] * 10 + digits[1] * 9 + digits[2] * 8 + digits[3] * 7 + digits[4] * 6 + digits[5] * 5 + digits[6] * 4 + digits[7] * 3 + digits[8] * 2 + digits[9] * 1) % 11 == 0