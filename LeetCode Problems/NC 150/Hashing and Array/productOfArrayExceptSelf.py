def productExceptSelf(self, nums: [int]) -> [int]: # Was not faster or more space saving then most but algorithmically it was O(N) in both
    #The trick to this one is to use the prefix, suffix method, but it's just some puzzle nonsense, I don't know maybe it serves a purpose but like damn it feels stupid.
    prefix = [1]
    postfix = [1]
    results = []

    for i in range(len(nums)):
        prefix.append(nums[i]*prefix[i])
    
    for i in range(len(nums)):
        postfix.append(nums[-i-1]*postfix[i])
    
    postfix.reverse()

    for i in range(len(nums)):
        results.append(prefix[i]*postfix[i+1])
    
    return results