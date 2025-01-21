# User function Template for python3

class Solution:
    def graphColoring(self, v, edges, m):
        # code here
        if v<=m:
            return True
        adj = {}
        for a,b in edges:
            adj[a] = adj.get(a,set())
            adj[a].add(b)
            adj[b] = adj.get(b,set())
            adj[b].add(a)
        
        groups = [set(range(v))]
        colored = set()
        while True:
            if len(colored)==v:
                break
            out=None
            pos=None
            for i in range(pos or 0,len(groups)):
                color = groups[i]
                pos = i
                for node in color:
                    if node in colored:
                        continue
                    colored.add(node)    
                    out = color.intersection(adj.get(node,set()))
                    if out:
                        groups[i] = color.difference(out)
                        if i==len(groups)-1:
                            groups.append(out)
                        else:
                            groups[i+1] = groups[i+1].union(out)
                        break
                if out:
                    break
        #print(groups)
        return len(groups)<=m
            
#{ 
 # Driver Code Starts
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges_input = list(map(int, input().split()))
        m = int(input())
        edges = []

        # Populate the edges list with edge pairs
        for i in range(0, len(edges_input), 2):
            edges.append((edges_input[i], edges_input[i + 1]))

        solution = Solution()
        print("true" if solution.graphColoring(n, edges, m) else
              "false")  # Call the graph coloring function
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends