class Solution:
    def longestCommonPrefix(self, strs) -> str:
        strs.sort(key=len)
        
        longestPrefix = ""
        
        matching = 1
        
        smallestWord = strs[0]
        
        for i in range(len(smallestWord)):
            
            if matching == 1:
            
                for j in range(len(strs)):

                    if smallestWord[i] != strs[j][i]:
                        matching = 0

            if matching == 1:
                longestPrefix += smallestWord[i]
        
        return longestPrefix