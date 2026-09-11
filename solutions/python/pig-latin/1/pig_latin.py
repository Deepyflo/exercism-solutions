vowels = "aeiou"

def translate_word(word):
    # Cas règle 1 : voyelle, xr, ou yt au début
    if word[0] in vowels or word[:2] in ("xr", "yt"):
        return word + "ay"

    # Cas règles 2, 3, 4 : trouver où couper
    for idx, letter in enumerate(word):
        if letter in vowels:
            split_index = idx
            break
        elif letter == "q" and word[idx + 1] == "u":
            split_index = idx + 2
            break
        elif letter == "y" and idx != 0:
            split_index = idx
            break
        else:
            split_index = len(word)  # aucune voyelle trouvée dans tout le mot

    return word[split_index:] + word[:split_index] + "ay"


def translate(text):
    words = text.split()
    translated_words = [translate_word(word) for word in words]
    return " ".join(translated_words)