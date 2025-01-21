class Trie:
    def __init__(self):
        self.node = [None]*26
        self.end = False

class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        def isConcatenated(word,t,start,op,path):
            print(path)
            if start == len(word) and len(path)>1:
                op.append(word)
                return True
            else:
                for i in range(start,len(word)):
                    c = ord(word[i])-97
                    if t.node[c] and t.node[c].end:
                        if isConcatenated(word,t,i+1,op,path+[word[start:i+1]]):
                            return True
                    elif t.node[c] is None:
                        break
                    t = t.node[c]
                    
        d = Trie()
        for word in words:
            n = len(word)
            t = d
            for i in range(n):
                c = ord(word[i])-97
                if not t.node[c]:
                    t.node[c]=Trie()
                if i == n-1:
                    t.node[c].end=True
                t = t.node[c]
        op = []
        for i in range(len(words)):
            isConcatenated(words[i],d,0,op,[])
        return op
    
if __name__ == "__main__":
    obj = Solution()
    obj.findAllConcatenatedWordsInADict(["catsdogcats","dogcatsdog","cat","cats","dog","hippopotamuses","rat","ratcatdogcat"])