def generateParenthesis(self, n: int) -> [str]: # I have to effectively implement this with a stack. So append and pop from a stack

    stack = []
    res = []

    def backtrack(openN, closedN): # This is the first time recursion has made more sense to me than an array 
        if openN == closedN == n:
            res.append("".join(stack))
            return res
        
        if openN < n:
            stack.append('(')
            backtrack(openN+1,closedN)
            stack.pop()

        if closedN < openN:
            stack.append(')')
            backtrack(openN, closedN+1)
            stack.pop()

    backtrack(0,0)

    return res
