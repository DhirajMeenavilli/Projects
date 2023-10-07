class Solution:
    def isPalindrome(self, head) -> bool:
        palindrome = []
        while head != None:
            palindrome.append(head.val)
            head = head.next
        palimdromeReverse = []
        
        for i in range(1,len(palindrome)+1):
            palimdromeReverse.append(palindrome[-i])
        
        return (palindrome == palimdromeReverse)