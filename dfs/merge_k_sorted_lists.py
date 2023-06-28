# Definition for singly-linked list.
import heapq
class ListNode:
    def __init__(self, val=0, nex=None):
        self.val = val
        self.nex = nex
    def __gt__(self, node):
        return self.val>node.val
    def __lt__(self, node):
        return self.val<node.val
    def __eq__(self, node):
        return self.val==node.val

class Solution:
    def mergeKLists(self, lists):
        heap = []
        res = None
        tail = None
        for l in lists:
            heap.append(l)
        heapq.heapify(heap)
        while len(heap):
            if not res:
                res = heapq.heappop(heap)
                tail = res
            else:
                tail.nex = heapq.heappop(heap)
                tail = tail.nex
            if tail.nex:
                heapq.heappush(heap,tail.nex)
            tail.nex = None
        return res

if __name__=='__main__':
    lists = [[1,4,5],[1,3,4],[2,6]]
    llists = []
    for i in range(len(lists)):
        llists.append(ListNode(lists[i][0]))
        last = llists[-1]
        for j in range(1,len(lists[i])):
            last.nex = ListNode(lists[i][j])
            last = last.nex
    slist = Solution().mergeKLists(llists)
    while slist:
        print(slist.val, end=" ")
        slist = slist.nex