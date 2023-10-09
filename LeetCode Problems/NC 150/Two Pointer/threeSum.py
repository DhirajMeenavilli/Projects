class Solution: # I ran into hell with this one because I made it l < len(nums), for some reason that caused the strangest behaviour, that I really cannot even begin to explain.
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()
        triplets = []
        duplicates = {}
        i = 0

        print(nums)

        while i < len(nums):
        
            l = i + 1
        
            r = len(nums) - 1

            while l < r:
                
                if nums[l] + nums[r] + nums[i] == 0: # It gets stuck in here because the value keeps equlaing 0 with no way to push either iterator out
                    if (nums[i], nums[l], nums[r]) in duplicates:
                        l += 1
                        pass

                    else:
                        
                        triplets.append([nums[i],nums[l], nums[r]])
                        
                        duplicates[(nums[i], nums[l], nums[r])] = 1
                        
                        l += 1

                elif nums[l] + nums[r] + nums[i] < 0:
                    
                    l += 1
                
                elif nums[l] + nums[r] + nums[i] > 0:
                    
                    r -= 1 

            i += 1
        
        return triplets