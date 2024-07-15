from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n  # Initialize the result array with zeros
        stack = []  # This will store the indices of temperatures

        for i in range(n):
            # While stack is not empty and the current temperature is higher than the temperature at the index stored at the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index  # Calculate the number of days
            stack.append(i)  # Push the current index onto the stack

        return result

# Example usage:
solution = Solution()
print(solution.dailyTemperatures([30, 38, 30, 36, 35, 40, 28]))  # Output: [1, 4, 1, 2, 1, 0, 0]
print(solution.dailyTemperatures([22, 21, 20]))  # Output: [0, 0, 0]
