def twoSum(self, nums, target):
    solution = []
    for i in range(len(nums)):
        new_num = target - nums[i]
        val = nums.pop(i)
        if new_num in nums:
            solution.append(i)
            solution.append(nums.index(new_num)+1)
            return solution
        nums.insert(i,val)