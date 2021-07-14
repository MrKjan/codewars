def sudoku(P):

    for row, col in [(r, c) for r in range(9) for c in range(9) if not P[r][c]]:
            
        rr, cc = (row // 3) * 3, (col // 3) * 3
            
        use = {1,2,3,4,5,6,7,8,9} - ({P[row][c] for c in range(9)} |
                                     {P[r][col] for r in range(9)} |
                                     {P[rr+r][cc+c] for r in range(3) for c in range(3)})

        if len(use) == 1:
            P[row][col] = use.pop()
            return sudoku(P)
    return P
