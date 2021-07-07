def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters_only = filter(lambda char: char.isalpha(), text)
    letters_as_digits = map(lambda char: str(1 + alphabet.find(char.lower())), letters_only)
    ret = ' '.join(letters_as_digits)
    return ret

print(alphabet_position('texT'))
