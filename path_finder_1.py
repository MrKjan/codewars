# https://www.codewars.com/kata/5765870e190b1472ec0022a2/train/python

def path_finder(maze):
    def neighbours(cells):
        ret = set(sum((((c[0]+1, c[1]),
                        (c[0]-1, c[1]),
                        (c[0], c[1]+1),
                        (c[0], c[1]-1)) for c in cells), ()))
        return ret

    walls = set()
    not_checked = set()
    checked = set()
    in_check = set()
    maze = maze.split('\n')
    for x, line in enumerate(maze):
        for y, row in enumerate(line):
            if (x, y) == (0, 0):
                in_check.add((0, 0))
                continue
            if maze[x][y] == '.':
                not_checked.add((x, y))
            if maze[x][y] == 'W':
                walls.add((x, y))
    
    while set() != in_check:
        neigh = neighbours(in_check)
        checked.update(in_check)
        in_check = set()
        for cell in not_checked:
            if cell in neigh:
                in_check.add(cell)
        not_checked = {cell for cell in not_checked if not cell in in_check}

    return True if (len(maze)-1, len(maze[-1])-1) in checked else False

a = "\n".join([
    ".W...",
    ".W...",
    ".W.W.",
    "...W.",
    "...W."])
print(path_finder(a))

a = "\n".join([
    ".W...",
    ".W...",
    ".W.W.",
    "...WW",
    "...W."])
print(path_finder(a))

a = "\n".join([
    "..W",
    ".W.",
    "W.."])
print(path_finder(a))

a = "\n".join([
    ".WWWW",
    ".W...",
    ".W.W.",
    ".W.W.",
    "...W."])
print(path_finder(a))

a = "\n".join([
    ".W...",
    "W....",
    ".....",
    ".....",
    "....."])
print(path_finder(a))

a = "\n".join([
    ".W",
    "W."])
print(path_finder(a))