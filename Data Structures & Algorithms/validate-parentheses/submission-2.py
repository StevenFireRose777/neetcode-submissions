class Solution:
    # Append only the left parenthesis
    def isValid(self, s: str) -> bool:
        stack = []
        matching = { "[": "]", "(": ")", "{": "}"}
        for char in s:
            if char == "[" or char == "{" or char == "(":
                stack.append(char)
            elif char == "]" or char == "}" or char == ")":
                if not stack:
                    return False
                popped_item = stack.pop()
                if matching[popped_item] != char:
                    return False
            



            # if char in matching:
            #     stack.pop() # Match found, pop the open bracket
            # else:
            #     return False
            
            
            
        if not stack:
            return True
        return False

                
        