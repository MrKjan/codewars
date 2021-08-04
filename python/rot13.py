def rot13(message):
    def shift_letter(letter):
        if not letter.isalpha():
            return letter

        if ord('a') <= ord(letter) <= ord('z'):
            first = ord('a')
        else:
            first = ord('A')

        return chr(((ord(letter) - first) + 13) % 26 + first)

    return ''.join(map(shift_letter, message))


print(rot13("Codewars")) # fails on 'T'
