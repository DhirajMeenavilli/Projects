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

def twoSum(nums:[int], target: int) -> [int]: #Slightly better code beats most people in memory, but less so in speed ~O(N^2), O(1) for memory.
    for i in range(len(nums)):
        if target - nums[i] in nums[i+1:]:
            return [nums.index(nums[i]), nums[i+1:].index(target - nums[i])+i+1]

def twoSum(self, nums: [int], target: int) -> [int]: #I like this solution more, it's a very clever trick. Not great on memory, but beats 70% of people in speed O(N) for both.
    store = {} #We are guaranteed a unique solution.
    for i in range(len(nums)):
        if target - nums[i] in store: # The trick to avoiding the duplicates is that we check if the difference first exists in the hash map then do the add, that way we avoid the issue of saying a number + itself is the solution, because it won't be the hashmap yet, and thus problem avoided.
            return [store[target-nums[i]],i]
        
        else:
            store[nums[i]] = i