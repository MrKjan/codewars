def duplicate_count(text):
    low = text.lower()
    repetitive = list(filter(lambda char: 1 < low.count(char), low))
    unique = set(repetitive)
    ret = len(unique)

    return ret

print(duplicate_count("AaaabbBbccCd")) # 0
