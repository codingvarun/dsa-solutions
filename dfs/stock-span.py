#https://practice.geeksforgeeks.org/problems/stock-span-problem-1587115621/1

class Solution:
    
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,a,n):
        #code here
        parent = [-1] #list to store the parent(last greater element) for each day stock price
        span = [] #final span list
        for i in range(1,n):
            if a[i]<a[i-1]:
                parent.append(i-1)
            else:                    
                #parent calculation using DFS
                par = parent[i-1]
                while par>=0:
                    if a[par]<=a[i]:
                        par = parent[par]
                    else:
                        break
                parent.append(par)

        for i in range(n):
            #span calculation by index difference between price and its parent
            span.append(i-parent[i])
        return span