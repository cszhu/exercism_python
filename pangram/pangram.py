def is_pangram(sentence):
    alphabet = []
    sentence = sentence.lower()
    for c in sentence:
        if c not in alphabet and c.isalpha():
            alphabet.append(c)
    if len(alphabet) == 26:
        return True
    return False
