from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Stack to store indices of the bars
        max_area = 0  # Variable to store the maximum area found
        index = 0  # Variable to iterate through the histogram bars

        while index < len(heights):
            # If the stack is empty or the current bar is taller/equal to the bar at the top of the stack, push its index onto the stack
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                # Pop the top of the stack
                top_of_stack = stack.pop()
                # Calculate the area with heights[top_of_stack] as the smallest (or minimum height) bar
                area = (heights[top_of_stack] * 
                       ((index - stack[-1] - 1) if stack else index))
                # Update max_area, if needed
                max_area = max(max_area, area)
        
        # Now, pop the remaining bars from stack and calculate area with every popped bar
        while stack:
            top_of_stack = stack.pop()
            area = (heights[top_of_stack] * 
                   ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)
        
        return max_area

# Example usage:
solution = Solution()
print(solution.largestRectangleArea([5, 6, 7, 2, 2, 4]))  # Output: 8
print(solution.largestRectangleArea([1, 3, 7]))  # Output: 7