from pyparsing import nestedExpr

class Calculator(object):
    def evaluate(self, data):
        def eval_no_brackets(data):
            def minuses_binary_to_unary(data):
                for idx, _ in enumerate(data):
                    if idx > 0 and '-' == data[idx] and data[idx-1].isdigit():
                        data.insert(idx, '+')
                return data

            def join_values(data):
                def is_digit(string):
                    for item in string:
                        if not item.isdigit() and item != '-':
                            return False
                    return True
                
                pass # TODO

            data = list(data)
            return str(eval(data))

        def _evaluate(data):
            if type(data) is str:
                return eval_no_brackets(data)
            elif type(data) is list:
                if 1 == len(data):
                    return _evaluate(data[0])
                else:
                    return _evaluate(''.join([_evaluate(item) if type(item) is list else item for item in data]))
        
        return _evaluate( nestedExpr().parseString(f'({data})').asList() )

# print(Calculator().evaluate("2 / (2) + 3*(4-1) - 6*(-4)"))
# print(Calculator().evaluate("(((-(0))+1))"))
# print(Calculator().evaluate("-1*1+-1*-1*1-1*1"))
# print(Calculator().evaluate("-1*-----1*--1"))
