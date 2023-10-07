def isPalindrome(s: str) -> bool:
    s = s.lower() # Lowers it so I don't have to worry about weirdness from upper case not matching upper case
    l,r = 0, len(s) - 1 # Setting the pointers at the start and end of the string

    while l < r: # While the pointers haven't met or outpaced one another

        while not s[l].isalnum() and l < len(s)-1: # If the pointer is pointing to something that's not alphanumeric there's no point comparing it against where the right pointer is
            l += 1
        
        while not s[r].isalnum() and r > 0: # THe sme logic as above applies here
            r -= 1
        
        if s[l].isalnum() and s[r].isalnum(): # Ran into a case where string was ".," so the entire thing was a non alphanumeric so like this lets me check like hey did the loops before stop because they ran into something alphanumeric, or cus they ran out of space to run.
            if s[l] != s[r]: # If they are both pointing to a number/letter and they're not the same then when the string is reversed there's no way the string and it's reveresed counter are going to be the same once non alphanumeric values are removed.
                return False # This is I think is the big trick of 2 pointers, just being if x[l] != whatever transformation of x[r] then it's valid or invalid depending on the problem. 
        
        l += 1
        r -= 1
    
    return True