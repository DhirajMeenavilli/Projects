def isValid(self, s: str) -> bool: # The second condition isn't satisfied by any of the test cases, So that's an edge case for sure. Also have to use stack somehow.
    # Maybe a stack at most n deep which lets go of the top of it's stack (LIFO) when a closing bracket of any kind appears and if they match then it's a valid thing, and do this until we have no more things to searh in which case
    # We return true, but if the stack is empty i.e no opening brackets and we encounter a closing bracket we return False, and if the stack is not empty but we're done the list i.e opening brackets with no closing brackets, then return false

    string = list(s)
    openings = ['(','[','{'] #Boys
    closings = [')',']','}'] #Girls don't need us but we always spawnibg with them L.
    stack = []

    for i in range(len(string)):
        print(string[i])
        if string[i] in openings:
            stack.append(string[i])

        if string[i] in closings: #Wait I did, think of this edge case of just a cloing with no opening and then forgot to code it. PFFTT.
            if len(stack) == 0:
                return False    
            
            check = stack.pop()
            
            if closings.index(string[i]) != openings.index(check): # This is defenitley the proggraming part where you're like ah shoot I gitta the computer to relaise a bracket is the vloser for an opener of the same kind, and you come up with some quick hack way of doing it.
                return False

    if len(stack) != 0:
        return False
    
    else:
        return True
