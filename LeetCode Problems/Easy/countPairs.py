nums = [-6,2,5,-2,-7,-1,3]
target = -2

l = 0
count = 0
while l < len(nums)-1:
    r = l + 1
    while r < len(nums):
        if nums[l] + nums[r] < target:
            print(l,r)
            count += 1
        r += 1
    l += 1

print(count) # This is an O(n^2) solution.