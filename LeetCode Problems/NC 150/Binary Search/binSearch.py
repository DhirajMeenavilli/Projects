# class Solution: I'm doing recursion entirely wrong, for some reason I can't pass a list back without causing some kind of hashing error, and I can't get a remote hold of the if else loops.
#     def search(self, nums: List[int], target: int) -> int:
        
#         if len(nums) == 0:
#             return -1

#         curr = len(nums) // 2

#         if nums[curr] == target:

#             return nums[curr]

#         else:

#             if nums[curr] > target:
#                 new_list = nums[:curr]
#                 curr = search(new_list, target)
#                 return curr
                
#             else:
#                 new_list = nums[curr:]
#                 print(curr)
#                 curr = search(new_list , target)
#                 return curr
        
#         if curr == -1:
#             return curr
        
#         else:
#             return nums.index(curr) But I know the algorithmic solution search for half then half again then half again until you get to the bottom of the tree and then just add and subtract from the value as needed when going up 


def search(self, nums: [int], target: int) -> int: # The logic of the algorithim is that if we eliminate the midway point then we eliminate everything before or after it, so we can then turn to the next half of the array we diidn't liminate, we're taking Xeno Steps.
    l = 0
    r = len(nums) - 1 # Bin Search the algorithim I learned so many times for school, and I could disect it in all sorts of ways, and explain it I couldn't implement it. 

    while l <= r: # Just a simple idea oh if the left pointers crossed the right pointer the array has 0% probability of finding the target so we can stop looking.
        m = (l + r)//2
        print(l,r,m)
        if nums[m] > target:
            r = m - 1
        
        elif nums[m] < target:
            l = m + 1
        
        elif nums[m] == target:
            return m
    
    return -1 # But yeah, I can't believe NeetCode essentially boiled it down to 7 mins and did it cleverly with two pointers, guess this is when I start asking through my checklist of datatypes and algorithims.


