# Not even remotely sure how the nums array in this case works, like what it's structure is to manipulate it, like even resetting it didn't change the output it was super weird, it was like a fundamental structure or sumin odd.
def removeDuplicates(self, nums: list[int]) -> int:
    l = 1

    for r in range(1, len(nums)):
        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l += 1
    
    return l