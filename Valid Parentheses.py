class Solution:
    def isValid(self, s: str) -> bool:
        # List to keep track of opening brackets
        open_brackets = []
        
        # Mapping of closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Iterate through each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Check if the list is empty or if the last element does not match the corresponding opening bracket
                if not open_brackets or open_brackets[-1] != bracket_map[char]:
                    return False
                # If it matches, pop the last element (this means the bracket is closed)
                open_brackets.pop()
            else:
                # If it's an opening bracket, append it to the list
                open_brackets.append(char)
        
        # If the list is empty, all opening brackets were matched correctly
        return not open_brackets
