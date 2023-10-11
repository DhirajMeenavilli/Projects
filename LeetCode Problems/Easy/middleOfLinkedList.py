class Solution:
    def middleNode(self, head):
        theList = head
        length = 0
        
        while head != None:
            head = head.next
            length += 1
        
        head = theList
        
        for i in range(length//2):
            head = head.next
            
        return head