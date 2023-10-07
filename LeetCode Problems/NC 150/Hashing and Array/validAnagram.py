def isAnagram(s: str, t: str) -> bool: #I like my solution the best.
    s = list(s)
    t = list(t)

    if len(s) != len(t):
        return False

    s.sort()
    t.sort()

    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    
    return True

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t): #Could do this with a counter or sorted object and just sorted(s) == sorted(t) or counter(s) == counter(t).
        return False
    
    countS, countT = {}, {} #Create Hashmap

    for i in range(len(s)):
        countS[s[i]] = countS.get(s[i],0) + 1 #We use .get to make sure a key error isn't thrown if the charachter doesn't exist in the string
        countT[t[i]] = countT.get(t[i],0) + 1
    
    for c in countS:
        if countS[c] != countT.get(c,0):
            return False
    
    return True