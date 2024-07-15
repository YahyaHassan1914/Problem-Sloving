from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(a / b))  # Division truncates toward zero

        return stack[0]

# Example usage:
tokens = ["1", "2", "+", "3", "*", "4", "-"]
solution = Solution()
print(solution.evalRPN(tokens))  # Output: 5
