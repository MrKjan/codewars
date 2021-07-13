def sort_array(source_array):
    if not source_array:
        return source_array
    odd_idx, odd = zip(*[tuple for tuple in enumerate(source_array) if tuple[1] % 2 == 1])
    odd_dict = dict(zip(odd_idx, sorted(list(odd))))
    return [val if val % 2 == 0 else odd_dict[idx] for idx, val in enumerate(source_array)]

print(sort_array([9,8,7,6,5,4,3,2,1,0]))

#try next(iter)
#try sorted reverse and pop
#https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/solutions/python
