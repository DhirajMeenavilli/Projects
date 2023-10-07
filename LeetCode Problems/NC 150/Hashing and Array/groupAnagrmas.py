def groupAnagrams(self, strs: [str]) -> [[str]]: #This was actually all me using boith the hashing structure, and the sorting structure so this O(M) * O(N log N) time, 
    # because we iterate the list of words once O(M), but then have to sort each list of strings O(N log N) and then join O(N), append O(1), and hash O(1) for that list which mean O(N) * O(M)
    # but then these are all effectively dominated by the sort which O(N log N) hence time complexity = O(M) * O(N log N), Space complexity of O(M) * O(N), I think(?).

    terms = {}
    sorted_terms_index = {}

    for i in range(len(strs)):
        terms[strs[i]] = list(strs[i]) # We append the list i.e broken up version of the string here.
        terms[strs[i]].sort() # Then we sort it to get the sorted version because if the sorted versions align we can say they are annagrams

    for i in range(len(strs)): # Was actually able to decrease the time taken beating ~70% of submissions by eliminating the join hence the extra O(N) by just setting it as a tuple, could probably do even better by setting it as a tuple even initally
        if tuple(terms[strs[i]]) in sorted_terms_index: # We do a join, just because you can't have an array as the key for a dictionary/hash
            sorted_terms_index[tuple(terms[strs[i]])].append(strs[i]) # We then if the joined string is already there simply append to a array which is the value assigned to that specific sorted order of the word, thus only anagrams would share the exact same order
        else:    
            sorted_terms_index[tuple(terms[strs[i]])] = [strs[i]] # We create the key: value pair i.e sorted order of words : [actual word] 
    
    keylist = list(sorted_terms_index.keys()) # We then retrieve all the keys of the dictionary

    list_of_anagrams= []

    for  key in keylist:
        list_of_anagrams.append(sorted_terms_index[key]) # This then is us putting the list of words associated with every ordered/sorted word into this array that we can return to user so they can see which words are anagrams.
    
    return list_of_anagrams

    # for i in range(len(strs)): # Funny enough this is where the idea started
    #     terms[strs[i]].sort() # Perhaps I can just sort all of them intially and then compare