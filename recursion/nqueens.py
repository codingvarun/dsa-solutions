from typing import *

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        positions = []            

        def setQueens(qrem,plcmnt,rset,cset):
            print(plcmnt)
            if qrem==0:
                positions.append(plcmnt)
            else:
                for r in rset:
                    for c in cset:
                        diag_taken = False
                        for i in range(n):
                            if ((r-i,c-i) in plcmnt) or ((r+i,c+i) in plcmnt):
                                diag_taken = True
                                break
                        if not diag_taken:
                            plcmnt.add((r,c))
                            rset.discard(r)
                            cset.discard(c)
                            setQueens(qrem-1,plcmnt,rset,cset)
                            plcmnt.discard((r,c))
                            rset.add(r)
                            cset.add(c)
        rs = set(range(n))
        cs = set(range(n))
        setQueens(n,set(),rs,cs)
        res = []
        for pos in positions:
            pos = list(pos)
            grid = [['.']*n for i in range(n)]
            for i,j in pos:
                grid[i][j] = 'Q'
            grid = [str(r) for r in grid]
            res.append(grid)
        
        return res

if __name__=='__main__':
    s = Solution()
    print(s.solveNQueens(4))  # [[".Q..","...Q","