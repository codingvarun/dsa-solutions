#User function Template for python3
class Solution:
    # Function to find all possible paths
    def findPath(self, mat):
        # code here
        def move(row,col,n,path,solutions,visited):
            if row==n and col==n:
                solutions.append(path)
                return
            if row+1<=n and mat[row+1][col]==1 and not ((row+1,col) in visited):
                move(row+1,col,n,path+'D',solutions,visited.union({(row,col)}))
            if row-1>=0 and mat[row-1][col]==1 and not ((row-1,col) in visited):
                move(row-1,col,n,path+'U',solutions,visited.union({(row,col)}))
            if col+1<=n and mat[row][col+1]==1 and not ((row,col+1) in visited):
                move(row,col+1,n,path+'R',solutions,visited.union({(row,col)}))
            if col-1>=0 and mat[row][col-1]==1 and not ((row,col-1) in visited):
                move(row,col-1,n,path+'L',solutions,visited.union({(row,col)}))

        solutions = []
        move(0,0,len(mat)-1,'',solutions,set((-1,-1)))
        return sorted(solutions)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        input_line = input().strip()
        mat = eval(input_line)

        solution = Solution()
        result = solution.findPath(mat)

        if not result:
            print("[]")
        else:
            print(" ".join(result))
        print("~")

# } Driver Code Ends