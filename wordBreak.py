class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        wordSet = set(wordDict)
        isBreakable = [None for i in range(len(s))]
        def breakWord(wordSet,isBreakable,start,word):
            if isBreakable[start] is not None:
                return isBreakable[start]
            for end in range(start+1,len(word)+1):
                if word[start:end] in wordSet:
                    if end == len(word):
                        isBreakable[start] = True
                    elif isBreakable[end] is not None:
                        isBreakable[start] = isBreakable[start] or isBreakable[end]
                    else:
                        isBreakable[start] = isBreakable[start] or breakWord(wordSet,isBreakable,end,word)
                    return isBreakable[start]
            return False
        breakWord(wordSet,isBreakable,0,s)
        return isBreakable[0]
    
if __name__=='__main__':
    s = Solution()
    print(s.wordBreak("applepenapple",\
                       ["apple","pen"])) # True