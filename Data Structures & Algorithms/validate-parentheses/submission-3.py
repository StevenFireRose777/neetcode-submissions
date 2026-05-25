class Solution:
    # Append only the opening parenthesis
    def isValid(self, s: str) -> bool:
        stack = []
        matching = { "[": "]", "(": ")", "{": "}"}
        for char in s:
            if char == "[" or char == "{" or char == "(":
                stack.append(char)
            elif char == "]" or char == "}" or char == ")":
                # If the char is only a closing bracket and no opening parenthesis were added
                if not stack:
                    return False
                popped_item = stack.pop()
                if matching[popped_item] != char:
                    return False
            
            
        if not stack:
            return True
        return False

                
        