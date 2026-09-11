def is_isogram(phrase):
    return len(phrase.replace(' ', '').replace('-', '').upper()) == len(set(phrase.replace(' ', '').replace('-', '').upper()))
