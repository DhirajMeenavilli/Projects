class Solution:
    def maxArea(self, height: [int]) -> int: # We can't sort it as we'd lose the order, and we want to use a left and right pointer somehow, brute force is just O(N^2) but whatever we can try it.

        store = []
        l = 0
        for i in range(len(height)): # If we can see what the furthest point that is <= to the current value, we could find the greatest distance for a given multiplied by the square of theheight itself gives you the volume. By starting the right pointer at the right and then pulling it down then resetting as we increase the left pointer after every iteration might be the way to go, don't need a hash, just an array should do. So this current solution works but it's O(N^2), so it exceeds time limit.
            r = len(height) - 1
            
            volume = 0
            
            while r >= l: # Probably shouldn't be a while but rather an if, there does need to be a while just not sure where
                
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