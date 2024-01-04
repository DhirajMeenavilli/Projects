"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0
"""
# Problem: Search an array such that the largest unidirectional nonnegative difference is reported.

# Structure of the Problem: An array with prices distributed unoformally randomly and the index location is taken as the day. The structure did not give me any reason to think that l and r should be upadted at the same time but I did nonetheless and it led to error in an edge case.

# You can rethink of this as blocks of varying brightness, and ourselves as travellers at the darkest spot seeing how bright the brightest point ahead of us is.
# We can do this by getting an O(n^2), by putting the travellers at the first block and seeing what block leads to the highest difference shifting the travellers forward everytime we reach the end.
# We can do it a bit quicker by taking everything after the block the travellers on and sorting it to be in descending order then take a difference and that will be the max difference that way we get it in O(n) + O(n * n log n).
# If there was a way to pick the best purchase day out of the array, this would only be possible if the array were not uniformly distributed, which is a feature that could be picked up by a ML model maybe?
# If you stood at the highest point on the hill and organised the blocks behind it and dropped a ball you could find their difference in O(n) + O(n log n)
# However this too fails because in the same way the smallest price is not neccessarily the best buy day, the highest price is not neccessarily the best sell day.
# Therefore the greatest difference can occur after the highest peak and before the lowest valley. 
# Also if I can just take the difference of every number after the number chosen and just return the largest it'd be the greatest differnce 
# This can be reduced to O(n) if the two pointers can be moved on some condition
prices = [7,6,4,3,1]

l = 0
r = 1
difference  = 0

# The question now is why would you move l or r, and the answer is because there is a greater difference to be had
# In a simpler question you would find just the smallest and largest number, in this instance you must find the largest backward difference
# We could move the left pointer if there's a smaller number on the right, this fails as we can easily hit local optima
# We could move the left pointer if it's larger than the right, while better still leads to local optima
#  

while r < len(prices):

    if prices[l] < prices[r]: 
        if (prices[r]-prices[l]) > difference:
            difference = prices[r]-prices[l]

    else:
        l = r # The trick was effectively that you intialise the pointers next to each other and have one tail the other
# The logic I think is that because you would have seen all differences from wherever the left pointer is to wherever the right
# is lower than the left if there's then a point at which greater than the max profits could be derrived, it would neccessarily be greater
# from the even lower point that right is at.           
    r += 1

print(difference)