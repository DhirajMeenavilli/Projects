class Solution:
    
    def evalRPN(self, tokens: [str]) -> int: # Now this is a fun problem again, not implement a min stack. Like huh?
        # We can defenitley use the stack to load paranthesis just like before but we have to figure oput how store and execute operations in order (I think it tells you order via like 3, 2, + meaning 3+2 so we could do with pointers, but I think stack wrks too, better probably.). Through recursion we could execute at ever deeper levels and then just return them and then we don't have to worry about how to deal with berackets in brackets.(Also Leetcode is defenitley the place to just feel clever, especially once you have a hint like stacks, very basic but enough to set you off and implement it, god bless NeetCode.)
        if len(tokens) == 0:
            return 0

        if len(tokens) == 1:# The trick was to relaise I didn't have to store multiplications I could just execute them on the last two elements of the stack and just pop em.
            return int(tokens[0])

        value = 0
        equation = [] # Now this is the real question of recursion is each one going to get it's own memory location or will the computer overwrite the memory location of the variable previously called equation. SO when we return it just either blanks the variable, or crashes out. I can see why people use VMs in case they crash their shit out. Doing something like that.
        # openings = ['(', '[', '{'] # THis is unhinged I need to figure out a way to avoid having to use so much memory on restating the same thing a thousand times over, wait there are no brackets, I don't need to recurse at all. Holy, wow that would've been painful.
        # closings = [')',']','}']
        
        operator = ['+',"-",'*','/'] # Have to use if for each and make sure to // when it says '/'.

        for i in range(len(tokens)): # Defenitley could make it faster if I could figure out how to use 2 pointers are something. 
        
            # if tokens[i] in openings: #It said it'd be valid always so I'm not gonna worry about weird parentheis in wrong order and stuf edge cases. Or like a close bracket with no open bracket
            #     evalRPN(self, tokens[i+1:])
            
            # if tokens[i] in closings:
            #     return value # We'll also have to see how it jumps to the end of the paraenthesis that's been finished computing, will be interesting.
            print(equation)

            if tokens[i] in operator: # Not sure how to calculate the value like 4,13,5,+,- so this gives value = 18 then value = -14, ok so I can just say value = a operator b then. 
                if tokens[i] == "+": # My ordering isn't quite right but I think it's second operator first, but for multiplication and addition it's commutitive so whatever
                    first = equation.pop()
                    second = equation.pop()
                    equation.append(first + second)
                    value = first + second
                
                if tokens[i] == "-":
                    first = equation.pop()
                    second = equation.pop()
                    equation.append(second - first)
                    value = second - first # Forgot to swap it

                if tokens[i] == "*":
                    first = equation.pop()
                    second = equation.pop()
                    equation.append(first * second)
                    value = first * second
                    
                if tokens[i] == "/":
                    first = equation.pop()
                    second = equation.pop()
                    equation.append(int(second /  first)) # Rounds down so it makes it -1.
                    value = int(second /  first)
            
            else:
                equation.append(int(tokens[i])) # If it fails, it's defenitley something to do with the recursion call and pass. It's gotta be cus the logic looks beautiful, I hope it works.

        return value