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