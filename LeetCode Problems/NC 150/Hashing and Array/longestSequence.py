#Defenitley need to revist

def longestConsecutive(nums: [int]) -> int:
    store = {}
    seq = 0

    for i in range(len(nums)):
        if nums[i] not in store:
            store[nums[i]] = 1
    
    keyValues = list(store.keys())

    for key in keyValues:
        if (key-1) not in store:
            print(key)
            override = 1
            while key + override in store:
                override += 1
            if override > seq:
                seq = override
    
    return seq