def topKFrequent(self, nums: [int], k: int) -> [int]: # Very good on space but because I'm probably using slightly inefficient data structures I'm ~ 8 ms slower than the 90 percentile guy
    store = {}
    inverted_store = {}

    for i in range(len(nums)): # We effectively use this for loop to populate a dictionary with value : frequency, key_value pairs
        if nums[i] in store:
            store[nums[i]] = store[nums[i]] + 1 
        else:
            store[nums[i]] = 1
    
    keyvalues = list(store.keys())

    for key in keyvalues: # This for loop is used to populate the dictionary with frequency : [numbers with said frequency]
        if store[key] in inverted_store:
            inverted_store[store[key]].append(key)
        else:
            inverted_store[store[key]] = [key] # Might be better to leave it as just a interger, because the solutions are unique potentially meaning that there is no multiple values for a given frequency
    
    most_frequent = list(inverted_store.keys()) # Get the keys, which are frequencies
    most_frequent.sort(reverse = True) # Sort them in descending order, so most frequent

    return_list = []

    for i in range(len(most_frequent)): # What they didn't test was something like most frequent = 2 and give me three values of highest frequency for ex. [1,2,3] and k = 2, but that's fine
        for j in inverted_store[most_frequent[i]]: # This is just to cope with the fact that unique does not mean that each frequency gets only one value
            return_list.append(j)

        if len(return_list) == k: # Just to avoid the fact that since the arrays can store multiple numbers we don't want the return list getting too big.
            return return_list
    
    return return_list