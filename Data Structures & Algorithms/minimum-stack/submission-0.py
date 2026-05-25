class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        del self.stack[-1]
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        my_min = self.stack[0]
        for num in self.stack:
            if my_min > num:
                my_min = num
        # print(f"Value of current_min is: {my_min}")
        return my_min
