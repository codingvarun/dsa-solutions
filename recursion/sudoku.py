class Solution:
    def solveSudoku(self, board) -> None:
        row_set = [set([str(v) for v in range(1,10)]).difference(set(board[i])) for i in range(9)]
        col_set = [set([str(v) for v in range(1,10)]).difference(set([board[i][j] for i in range(9)]))\
                                                             for j in range(9)]
        sq_set = [[None]*3 for i in range(3)]
        for i in range(3):
            for j in range(3):
                sq_set[i][j] = set([str(v) for v in range(1,10)])
                for r in range(i*3,(i+1)*3):
                    for c in range(j*3,(j+1)*3):
                        sq_set[i][j].discard(board[r][c])
        blanks = []
        sudo = [['.']*9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    blanks.append((i,j))
                else:
                    sudo[i][j]=board[i][j]
        
        def solve(sudo,board,blanks,row_set,col_set,sq_set):
            if not blanks:
                for i in range(9):
                    for j in range(9):
                        board[i][j]=sudo[i][j]
                return True
            i,j=blanks[0]
            options = (row_set[i].intersection(col_set[j])).intersection(sq_set[i//3][j//3])
            if not options:
                return False
            else:
                for option in options:
                    sudo[i][j]=option
                    row_set[i].discard(option)
                    col_set[j].discard(option)
                    sq_set[i//3][j//3].discard(option)
                    if solve(sudo,board,blanks[1:],row_set,col_set,sq_set):
                        return True
                    row_set[i].add(option)
                    col_set[j].add(option)
                    sq_set[i//3][j//3].add(option)
        solve(sudo,board,blanks,row_set,col_set,sq_set)
            
            
if __name__=='__main__':
    s = Solution()
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    s.solveSudoku(board)
    print("OUTPUT")
    for row in board:
        print(row)