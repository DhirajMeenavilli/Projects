# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        value = ""
        value2 = ""
        
        length = 0
        length2 = 0
        
        testList = l1
        testList2 = l2
        
        while testList != None:
            testList = testList.next
            length += 1
        
        while testList2 != None:
            testList2 = testList2.next
            length2 += 1
        
        for i in range(length):
            value += str(l1.val)
            l1 = l1.next
            
        value = list(value)
        value.reverse()
        value = "".join(value)
        value = int(value)
        
        for i in range(length2):
            value2 += str(l2.val)
            l2 = l2.next
            
        value2 = list(value2)
        value2.reverse()
        value2 = "".join(value2)
        value2 = int(value2)
        
        summand = value + value2
        
        summand = list(str(summand))
        summand.reverse()
        
        output.val = summand[0]
        dummyList = output
        
        for i in range(1,len(summand)):
            
            # output.next = ListNode(summand[i])
            output = output.next
            
                
        output = dummyList            
        return (output)
