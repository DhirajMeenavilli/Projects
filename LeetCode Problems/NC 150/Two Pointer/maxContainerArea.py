class Solution:
    def maxArea(self, height: [int]) -> int: # We can't sort it as we'd lose the order, and we want to use a left and right pointer somehow, brute force is just O(N^2) but whatever we can try it.

    # We can defenitley still use left and right pointers, but the fact that each unit drop in vert is = a loss of height[l] and so is each unit drop in length means that we can stop searching very quickly because we can just check ok can the tonext value even at maximum be greater than the current volume if not then we can stop searching cus any point behind that is also going to be impossible to be greater than. For ex. with test case 1, we have 8 at the second position and 7 at the 9th position so at most at the 8th position we could get 8*(8-2) = 46 but 7*(9-2) = 49 therefore even using the max height it can't be beat thus we can stop searching.
        store = []

        l = 0

        for i in range(len(height)):
            r = len(height) - 1
                
            volume = 0
                
            while (r >= l) and (height[l] * (r-l) > volume): # Probably shouldn't be a while but rather an if, there does need to be a while just not sure where
                    
                # if height[r] >= height[l]:
                    
                if height[l] >= height[r]:
                    # print(height[r], height[l],r,l,r-l)
                    current_volume = height[r] * (r-l)
                    
                elif height[l] <= height[r]:
                    # print(height[r], height[l],r,l,r-l)
                    current_volume = height[l] * (r-l)
                    
                if current_volume > volume:
                    volume = current_volume
                
                r -= 1
                    
            l += 1 # Could instead use i, will do after
            
            store.append(volume)
        print(store)    
        return max(store) 

class Solution:
    def maxArea(self, height: [int]) -> int: # We can't sort it as we'd lose the order, and we want to use a left and right pointer somehow, brute force is just O(N^2) but whatever we can try it.

    # We can defenitley still use left and right pointers, but the fact that each unit drop in vert is = a loss of height[l] and so is each unit drop in length means that we can stop searching very quickly because we can just check ok can the tonext value even at maximum be greater than the current volume if not then we can stop searching cus any point behind that is also going to be impossible to be greater than. For ex. with test case 1, we have 8 at the second position and 7 at the 9th position so at most at the 8th position we could get 8*(8-2) = 46 but 7*(9-2) = 49 therefore even using the max height it can't be beat thus we can stop searching.
    
        l = 0
        r = len(height) - 1    
        volume = 0

        max_height = max(height)

        for i in range(len(height)):
            # while (r > l) and (height[l] * (r-l) > volume): # Probably shouldn't be a while but rather an if, there does need to be a while just not sure where
            # if max(height[l], height[r]) * (r-l) > volume # Thre's defenitley a clever stopping condition that lets you know like hey you've reached the point past which yea it's done, so probably using max(height), get the max value and then just if that max * (r-l) < volume just stop
            if (max_height * (r-l)) > volume:
                if height[l] <= height[r]:
                    
                    if (height[l] * (r-l)) > volume:
                        volume = height[l] * (r-l)
                    
                    l += 1
            
                elif height[l] >= height[r]:
                    
                    if (height[r] * (r-l)) > volume:
                        volume = height[r] * (r-l)
                        
                    r -= 1
            else:
                return volume
        return volume 