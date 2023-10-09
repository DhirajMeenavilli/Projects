class Solution:
    def twoSum(numbers: [int], target: int) -> [int]:# Slower than most, and less space efficient, but I love it, I really learned the nitty gritty of two pointers for sure, I'm gonna watch the video tommorow and get absolutely cooked.
        print(numbers)
        store = {} # We can append eacvh unique item and up the count of said value by 1 by and that should effectively tell us where the indexes are, because it is in sorted order so we can use that to basically jump, it's still n ^2 but on a considerably smaller hash set thats possibly a fraction of the value, though this can't account for multiple occurences of the value being the solution. Actually I guess if we see if the value associated with the shit is > 1 and it == target then we can just return the first and second index of the value

        for i in range(len(numbers)):
            if numbers[i] in store:
                store[numbers[i]] = store[numbers[i]] + 1
            
            else:
                store[numbers[i]] = 1
        
        keyValues = list(store.keys())
        
        l_iterator = 0

        while l_iterator < len(keyValues):
            
            l = keyValues[l_iterator]
            if store[l] >= 2:

                if l * 2 == target:
            
                    if keyValues.index(l) == 0:
                        return[1,2]
                    
                    else: # Didn't account for the duplicates not being first thing the same way, like I didn't come back and update it.
                        l_index = 0

                        for i in range(keyValues.index(l)): # This is some weird code man
                            l_index += store[keyValues[i]]
                        
                        return[l_index + 1, l_index + 2]

            r_iterator = len(keyValues) - 1 # Ok now looks really good

            while r_iterator > l_iterator:
            
                r = keyValues[r_iterator] # Forced to make it more efficient so I don't have to rely on r.

                if l + r == target: # This would normally take O(N^2) time but the fact that it's ordered might be really helpful 

                    l_index = 0
                    r_index = 0

                    for i in range(keyValues.index(r)): # less eficient than if I subtrated off the l index and just added whatevver remained in the distance to the r_index but it's fine
                        r_index += store[keyValues[i]]
                    
                    if l_iterator == 0: # Was using l_index instead of l_iterator, simple syntax slip
                        return [l_index + 1, r_index + 1]

                    else:
                        for i in range(keyValues.index(l)): # This is some weird code man
                            l_index += store[keyValues[i]]

                        return[l_index + 1, r_index + 1] # In the thing I need I need to get the sum of all values that come before but for now I think just sticking to 1 before is ok.
                
                r_iterator -= 1
            
            l_iterator += 1

        return [0,0]

def twoSum(numbers: [int], target: int) -> [int]: # The wildly more simple way of doing it, but it's just a bit slower, between 5 and 10 senonds, but space complexity is O(1).
    l = 0
    r = len(numbers) - 1

    for i in range(len(numbers)):
        if numbers[l] + numbers[r] == target:
            return [l+1, r+1]
        
        elif numbers[l] + numbers[r] < target:
            l += 1
        
        elif numbers[l] + numbers[r] > target:
            r -= 1