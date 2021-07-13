#***************************************************
#***************** Recursion ***********************
#***************************************************

# https://habr.com/ru/post/158385/
class recursion(object):
    "Can call other methods inside..."
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        while callable(result): result = result()
        return result

    def call(self, *args, **kwargs):
        return lambda: self.func(*args, **kwargs)


@recursion
def sum_natural(x, result=0):
    if x == 0:
        return result
    else:
        return sum_natural.call(x - 1, result + x)

# Даже такой вызов не заканчивается исключением
# RuntimeError: maximum recursion depth exceeded
# print(sum_natural(6000000))

# _____________________________

puzzle_example = [[5,3,0,0,7,0,0,0,0],
                  [6,0,0,1,9,5,0,0,0],
                  [0,9,8,0,0,0,0,6,0],
                  [8,0,0,0,6,0,0,0,3],
                  [4,0,0,8,0,3,0,0,1],
                  [7,0,0,0,2,0,0,0,6],
                  [0,6,0,0,0,0,2,8,0],
                  [0,0,0,4,1,9,0,0,5],
                  [0,0,0,0,8,0,0,7,9]]

# Copy from here
from queue import Queue
class Sudoku():
    def __init__(self, puzzle) -> None:
        self.todo = Queue()
        self.puzzle = puzzle
        self.done = {}
        for ii in range(9):
            for jj in range(9):
                cell = (ii, jj)
                if 0 == puzzle[ii][jj]:
                    self.todo.put_nowait(cell)
                    self.puzzle[ii][jj] = (1,2,3,4,5,6,7,8,9)

    def solve(self):
        cnt = 0
        while(True):
            if 0 == self.todo.qsize():
                return self.puzzle
            else:
                item = self.todo.get_nowait()
                values = self.compute_possible_values(item)
                if type(values) is int or len(values) < len(self.puzzle[item[0]][item[1]]):
                    self.puzzle[item[0]][item[1]] = values
                    cnt = 0
                else:
                    cnt += 1
                if type(values) is int:
                    self.done[item] = values
                else:
                    self.todo.put_nowait(item)

    def show(self):
        for ii in range(9):
            for jj in range(9):
                print(self.puzzle[ii][jj], end=' ')
            print()

    def compute_possible_values(self, item):
        old_values = self.puzzle[item[0]][item[1]]
        dependent_values = self.get_dependent_cell_values(item)
        diff = list(filter(lambda value: value not in dependent_values, old_values))
        return diff if len(diff) > 1 else diff[0]

    def get_dependent_cells(self, item):
        x = item[0]
        y = item[1]
        X = (x//3)*3
        Y = (y//3)*3
        return {
            (x, 0), (x, 1), (x, 2), (x, 3), (x, 4), (x, 5), (x, 6), (x, 7), (x, 8),
            (0, y), (1, y), (2, y), (3, y), (4, y), (5, y), (6, y), (7, y), (8, y), 
            (X+0, Y+0), (X+1, Y+0), (X+2, Y+0),
            (X+0, Y+1), (X+1, Y+1), (X+2, Y+1),
            (X+0, Y+2), (X+1, Y+2), (X+2, Y+2)
        }

    def get_dependent_cell_values(self, item):
        dependent_cells = self.get_dependent_cells(item)
        dependent_cells.remove(item)
        ret = set()
        for dep_cell in dependent_cells:
            if type(self.puzzle[dep_cell[0]][dep_cell[1]]) is int:
                ret.add(self.puzzle[dep_cell[0]][dep_cell[1]])
        return ret

def sudoku(puzzle):
    sdk = Sudoku(puzzle)
    sdk.solve()
    # sdk.show()
    return(sdk.puzzle)

# End of copy zone
print(sudoku(puzzle_example))
