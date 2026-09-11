def rotate(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "abcdefghijklmnopqrstuvwxyz".upper()
    cipher = alphabet[key:] + alphabet[:key]

    result = ""
    
    for letter in text:
        if letter.isupper():
            index_in_alphabet = alphabet_upper.index(letter)
            result += cipher[index_in_alphabet].upper()
        elif letter in alphabet:
            index_in_alphabet = alphabet.index(letter)
            result += cipher[index_in_alphabet]
        else:
            result += letter

    return result