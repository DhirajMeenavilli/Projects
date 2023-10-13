class MinStack: # There's no trick in this it's just doing the task, cus sometimes it's not a clever trick you just have to implement some non built in data structure tht's more efficient. Or use a library, but whatever, it's also good to know I guess.

    def __init__(self): # I was wrong, because school killed my creativity but the clever trick to this one was just to implement two arrays and use them in combination to do the min stack
        self.stack = []
        self.min = []
        self.curr_min = 0

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.curr_min = val

        self.stack.append(val)

        if self.curr_min >= val:
            self.curr_min = val
        
        self.min.append(self.curr_min)

    def pop(self) -> None:
        self.min.pop()
        if len(self.min) > 0:    
            self.curr_min = self.min[len(self.min)-1]
        else:
            self.currr_min = float('inf')

        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.min[len(self.min)-1]