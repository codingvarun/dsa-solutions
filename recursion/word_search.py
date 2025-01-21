from typing import *
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        l = len(word)

        def search(i,j,p,s,seq):
            print(s)
            print(seq)
            if not s:
                s = set()
            if p==l:
                return True
            elif board[i][j]==word[p]:
                match = False
                for r,c in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if match:
                        return match
                    if r>-1 and r<n and c>-1 and c<m and not (r==i and c==j) and not((r,c) in s):
                        s.add((r,c))
                        match = match or search(r,c,p+1,s,seq+word[p])
                        s.remove((r,c))
                return match
            else:
                return False
                        
        starts = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==word[0]:
                    starts.append((i,j))
        for i,j in starts:
            if search(i,j,0,{(i,j)},''):
                return True
        return False
    
if __name__ == '__main__':
    s = Solution()
    s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE")