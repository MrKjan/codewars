from pyparsing import nestedExpr

class Calculator(object):
    def evaluate(self, data):
        def eval_no_brackets(data):
            def minuses_binary_to_unary(data):
                for idx, _ in enumerate(data):
                    if idx > 0 and '-' == data[idx] and data[idx-1].isdigit():
                        data.insert(idx, '+')
                return data

            def is_digit(string):
                for item in string:
                    if not item.isdigit() and item != '-':
                        return False
                return True

            def join_values(data):
                idx = 0
                while idx < len(data):
                    if idx + 1 < len(data) and is_digit(data[idx]) and is_digit(data[idx+1]):
                        data[idx] = data[idx] + data[idx + 1]
                        data.pop(idx+1)
                    else:
                        idx += 1
                
                return data

            data = list(data)
            join_values(minuses_binary_to_unary(data))
            data = [i[i.count('-')//2*2:] if is_digit(i) else i for i in data]
            
            idx = 0
            while idx < len(data):
                if idx+1 >= len(data):
                    break
                if data[idx+1] == '*':
                    data[idx] = str(int(data[idx]) * int(data[idx+2]))
                    data.pop(idx+1)
                    data.pop(idx+1)
                elif data[idx+1] == '/':
                    data[idx] = str(int(int(data[idx]) / int(data[idx+2])))
                    data.pop(idx+1)
                    data.pop(idx+1)
                else:
                    idx += 1
            
            ret = str(sum([int(item) for item in data if item != '+'], 0))

            return ret

        def _evaluate(data):
            if type(data) is str:
                return eval_no_brackets(data)
            elif type(data) is list:
                if 1 == len(data):
                    return _evaluate(data[0])
                else:
                    return _evaluate(''.join([_evaluate(item) if type(item) is list else item for item in data]))
        
        def parse_nested_expr(self, string):
            def get_bracket_pair_pos(string):
                if open := string.find('(') < 0:
                    return -1, -1
                count = 1
                for idx, item in enumerate(string[open+1:]):
                    if '(' == item:
                        count += 1
                    if ')' == item:
                        count -= 1
                    if 0 == count:
                        break
                else:
                    return open, -1
                return open, open + idx

            pass
        
        return _evaluate( nestedExpr().parseString(f'({data})').asList() )

print(Calculator().evaluate("(4-1)"))
print(Calculator().evaluate("2 / (2) + 3*(4-1) - 6*(-4)"))
print(Calculator().evaluate("(((-(0))+1))"))
print(Calculator().evaluate("-1*1+-1*-1*1-1*1"))
print(Calculator().evaluate("-1*-----1*--1"))
