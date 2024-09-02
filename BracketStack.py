class Solution:
    def isValid(self, s: str) -> bool:
        char_stack = []
        char_map = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in char_map:
                if not char_stack or char_stack.pop() != char_map[char]:
                    return False
            else:
                char_stack.append(char)
        return not char_stack