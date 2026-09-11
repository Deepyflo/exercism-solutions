def is_pangram(sentence):
    alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    sentence = sentence.upper()
    
    unique_sentence = set(sentence)

    return len(alphabet.intersection(unique_sentence)) == 26