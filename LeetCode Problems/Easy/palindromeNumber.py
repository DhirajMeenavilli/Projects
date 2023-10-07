class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = list(str(x))
        a.reverse()
        print(a)
        if ''.join(a) == str(x):
            return True
        
        else:
            return False