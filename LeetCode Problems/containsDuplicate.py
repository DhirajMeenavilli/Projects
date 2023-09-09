import math

def heapify(arr):
    n = len(arr)

    # Start from the last non-leaf node and move towards the root
    for i in range(n // 2 - 1, -1, -1):
        heapify_down(arr, n, i)

def heapify_down(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Compare with left child
    if left < n and arr[left] < arr[smallest]:
        smallest = left

    # Compare with right child
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    # Swap with the smallest child and continue heapify_down
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify_down(arr, n, smallest)

exit = False
duplicates = False

heapify(nums)

i=0

while exit == False:
    copy = []
    try:
        for j in range(2**i):
            copy.append(nums[2**i - 1 + j]) #Appended the top layer

        for l in range(len(copy)):
            for k in range(2**(i+1)):                
                if (nums[2**(i+1)+k-1] in copy):
                    duplicates = True

        if duplicates:
            exit = True 
        
        i += 1
    
    except Exception: # Do on second last level and create another loop which checks just the last layer. Basically what this is.
        start = int(math.log(len(nums))/math.log(2)) + 1 # Can put in exception

        for i in range(start, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == nums[i]:
                    duplicates = True

        exit = True




if duplicates:
    print("True")

else:
    print("False")

# """
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true

# Example 2:

# Input: nums = [1,2,3,4]
# Output: false

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

 

# Constraints:

#     1 <= nums.length <= 105
#     -109 <= nums[i] <= 109

# Accepted
# 3.2M
# Submissions
# 5.2M
# Acceptance Rate
# 61.0%
# """

# #1. Build the tests of the main code. 2. Create a simmulation / thing (like the combinatorail communication station)where this would happen, and ask a question. 3. Answer the question thinking about this cool weird world where sonic rings randomly and spontaneously fall on pegs and so on.
# #If there's 2 in the array a search or sort couldn't really detect it, but there must be some data structure which has the same numbers together, (Clever brute force on a tree? should reduce it from whatever terrible intial idea I had)
# def heapify(arr):
#     n = len(arr)

#     # Start from the last non-leaf node and move towards the root
#     for i in range(n // 2 - 1, -1, -1):
#         heapify_down(arr, n, i)

# def heapify_down(arr, n, i):
#     smallest = i
#     left = 2 * i + 1
#     right = 2 * i + 2

#     # Compare with left child
#     if left < n and arr[left] < arr[smallest]:
#         smallest = left

#     # Compare with right child
#     if right < n and arr[right] < arr[smallest]:
#         smallest = right

#     # Swap with the smallest child and continue heapify_down
#     if smallest != i:
#         arr[i], arr[smallest] = arr[smallest], arr[i]
#         heapify_down(arr, n, smallest)

# # def search_heap(arr, index, target, depth=0): I just realised a sorted list has the duplicates right next to one another
# #     while 

# #     left_child_index = 2 * index + 1
# #     right_child_index = 2 * index + 2

# #     # Recursively search in the left subtree
# #     left_found, left_depth = search_heap(arr, left_child_index, target, depth + 1)

# #     # If found in the left subtree, return immediately
# #     if left_found:
# #         return True, left_depth

# #     # Otherwise, search in the right subtree
# #     right_found, right_depth = search_heap(arr, right_child_index, target, depth + 1)

# #     # Return the result from the right subtree
# #     return right_found, right_depth

# # Example usage:

# #Easy way out: Just search the array keeping another array with every number come across and see if the current number you're on in the actual array is in the other array. Return true if yes
# import math

# output = [4, 7, 1, 2, 6, 5, 9, 10, 8, 12, 11,10]
# heapify(output)
# print(output)
# # search, depth = search_heap(output, 0, 4)
# duplicates = False
# i=0
# copy = [2, 4]
# exit = False
# print(4 in output)
# while exit == False:
#     copy = []
#     try:
#         for j in range(2**i):
#             copy.append(output[2**i - 1 + j]) #Appended the top layer

#         for l in range(len(copy)):
#             for k in range(2**(i+1)):                
#                 if (output[2**(i+1)+k-1] in copy):
#                     duplicates = True

#         if duplicates:
#             exit = True 
        
#         i += 1
    
#     except Exception: # Do on second last level and create another loop which checks just the last layer. Basically what this is.
#         print("Flagged")
#         start = int(math.log(len(output))/math.log(len(output))) + 1 # Can put in exception

#         for i in range(start, len(output)):
#             for j in range(i+1, len(output)):
#                 if output[j] == output[i]:
#                     duplicates = True

#         exit = True




# if duplicates:
#     print("Duplicates")

# else:
#     print("No Duplicates")
#                         # LUCKKKYYYY, the numbers in the array are arranged in node order.
# try:                   #The listed below are node numbers I have to decipher where the node will be in the array, which is prolly pre doabble, and then I need to figure out how to get the loop to search it.
#     if(output == []): # I got what I'm doing, duplicate if it's on the same level or just 1 below which is what seems most likely to be based on which node it is it can check up to the node directly to the left and right of it so Level 0 : (0 and 1 and 2), Level 1: (1 and 2 and 3 and 4, just checking your own children is good, you're probalisticly not gonna miss em) Twice, but the second time searching for the value at node 2, Level 2:(3 and 4 and 5 and 6 and and 7 and 8)
#         print("Holy shit it's working.")#I need to get it it to search from 0-2, 1-2-3-4, 2-5-6, 3-4-5-6-7-8, 4-5-6-9-10, 5-6-11-12, 6-13-14 #It would be easier if I just searched the full level and the next level keeping just an array of the current level, than I just go 0-2, 2, record level starting at 2^i - 1 and continuing 2^i - 1 times, still probablistic but less efficient, but that's an improvement I can make
    
# except Exception:
#     print("oh nart!")