from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = [("", 0, 0)]
        
        while stack:
            current, open_count, close_count = stack.pop()
            
            if len(current) == n * 2:
                result.append(current)
                continue
            
            if open_count < n:
                stack.append((current + "(", open_count + 1, close_count))
            
            if close_count < open_count:
                stack.append((current + ")", open_count, close_count + 1))
        
        return result

# Example usage:
solution = Solution()
print(solution.generateParenthesis(1))  # Output: ["()"]
print(solution.generateParenthesis(3))  # Output: ["((()))","(()())","(())()","()(())","()()()"]
