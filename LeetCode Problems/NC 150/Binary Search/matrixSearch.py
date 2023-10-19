# def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: # Got the basic idea right I think reduce it from a double binary search to a single binary search done twice, first to locate the array, then again inside that array.
#     l1 = 0 
#     # l2 = 0 # matrix[l1][l2]
#     r1 = len(matrix) -1
#     # r2 = [len(matrix[len(matrix) -1])-1] I'm not really uising these
    
#     i = 0

#     while l1 < r1: # Might need <=
#         mid1 = (r1 - l1) // 2
#         mid2 = len(matrix[mid1]) // 2 # Can't just constantly // 2, because then unless the target is dead smack in the array you wind up at you'll miss it

#         if matrix[mid1][mid2] > target:
#             r1 = mid1
#             #Find the halfway point of the remaning array
        
#         elif matrix[mid1][mid2] < target:
#             l1 = mid1
        

#     print(l1,r1)
    
#     l2 = 0
#     r2 = len(matrix[mid1])

#     while l2 < r2:
#         mid2 = (r2-l2) // 2
#         print(mid2)
#         if matrix[mid1][mid2] > target:
#             r2 = mid2
        
#         elif matrix[mid1][mid2] < target:
#             l2 = mid2
        
#         elif matrix[mid1][mid2] == target:
#             return True

# class Solution: Generally ok, better algorithimically but amakes me realise I'm just getting the snot beat out of me as a proggrammer
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
#         l = 0
#         r = len(matrix) - 1

#         while l < r:
#             mid = (l+r)//2

#             if matrix[mid][0] > target:
#                 r = mid
            
#             elif matrix[mid][len(matrix[mid])-1] < target:
#                 l = mid

#             else:
#                 l,r = mid, mid

#         if len(matrix) > 1:
#             arr = matrix[mid]
        
#         else:
#             arr = matrix[0]

#         print(arr)
#         l = 0
#         r = len(arr) - 1

#         while l != r -1:
#             mid = (l+r)//2

#             if arr[mid] > target:
#                 r = mid

#             elif arr[mid] < target:
#                 l = mid
            
#             else:
#                 return True
        
#         if len(arr) > 2:
#             return False
        
#         if len(arr) > 1:
#             if arr[0] == target or arr[1] == target:
#                 return True
            
#             else:
#                 return False
        
#         if len(arr) > 0:
#             if arr[0] == target:
#                 return True
        
#             else:
#                 return False

#         if len(arr) == 0:
#             return False

# Awful Sol:

class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool: 
        l = 0
        r = len(matrix) - 1

        while l < r:
            mid = (l+r)//2

            if matrix[mid][0] > target:
                r = mid
            
            elif matrix[mid][len(matrix[mid])-1] < target:
                if l == mid:
                    mid += 1
                    break

                l = mid

            else:
                l,r = mid, mid

        if len(matrix) > 1:
            arr = matrix[mid]
        
        else:
            arr = matrix[0]

        print(arr)
        l = 0
        r = len(arr) - 1

        while l < r -1:
            mid = (l+r)//2

            if arr[mid] > target:
                r = mid

            elif arr[mid] < target:
                l = mid
            
            else:
                return True

        if len(arr) > 2:
            if arr[l] == target:
                return True
            
            if arr[r] == target:
                return True

            return False
        
        if len(arr) > 1:
            if arr[0] == target or arr[1] == target:
                return True
            
            else:
                return False
        
        if len(arr) > 0:
            if arr[0] == target:
                return True
        
            else:
                return False

        if len(arr) == 0:
            return False