def is_isogram(string):
    #things do not repeat
    alphabet = {}
    string = string.lower()
    for c in string:
        if (c.isalpha()) == True:
            if c not in alphabet:
                alphabet[c] = c
            else:
                return False
    return True
