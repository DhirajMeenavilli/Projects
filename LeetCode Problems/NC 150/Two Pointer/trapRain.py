def trap(self, height: [int]) -> int:
    # The way to calculate the amount of water trappable at any location, is the min(L,R) - height[i], which if > 0 stores water = whatever the operation yields. So that's one really clever math trick. 
    # But then I can't even implement because I don't know how to even intialise and move the left and right pointers. Should be very good in shedding some light. 
    # Using an array we could in O(N*3) scan through and put the largest heights on the left adn right, and then just take them min of the two arrays, thus leetting us do the question. 
    # But how to do with 2 pointers? 

    store = []

    max_left = []
    max_right = []
    
    l = 0
    r = 0

    for i in range(len(height)):
        if height[i] > l:
            l = height[i]

        max_left.append(l)

        if height[-i-1] > r:
            r = height[-i-1]
        
        max_right.append(r)
    
    max_right.reverse()

    for i in range(len(height)):
        if min(max_left[i],max_right[i]) - height[i] > 0:
            store.append(min(max_left[i],max_right[i])- height[i])
    
    return sum(store)

def trap(self, height: [int]) -> int: # Defeniley need to come back and look at so that I can rework the solution to makle sense to me
    #Turns out you can do it with intialiseing the pointers at the end of the array, and just moving the smaller one, while keeping track of the largest value from each pointer, then moving the smaller one, as the smaller one is basically always going to be the bottleneck, hence we can move it.
    if len(height) == 0:
        return 0

    l = 0
    r = len(height) - 1

    max_left = height[l]
    max_right = height[r]

    water = 0
    # i = 0
    while r > l:
        if max_left > max_right:
            r -= 1
            max_right = max(max_right, height[r])
            water += max_right - height[r]

        else:
            l += 1
            max_left = max(max_left, height[l])
            water += max_left - height[l]
        
        # if min(max_left, max_right) - height[i] > 0: # Check the amount water that can be stored
        #     water += min(max_left, max_right) - height[i]
        
        
        # if height[l] > max_left:
        #     max_left = height[l]
        
        # if height[r] > max_right:
        #     max_right = height[r]

        # i += 1

    return water