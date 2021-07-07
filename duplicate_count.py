def duplicate_count(text):
    low = text.lower()
    repetitive = list(filter(lambda char: 1 < low.count(char), low))
    unique = set(repetitive)
    ret = len(unique)

    return ret

print(duplicate_count("AaaabbBbccCd")) # 0

# print(duplicate_count("")) # 0
# print(duplicate_count("abcde")) # 0
# print(duplicate_count("abcdeaa")) # 1
# print(duplicate_count("abcdeaB")) # 2
# print(duplicate_count("Indivisibilities")) # 2

