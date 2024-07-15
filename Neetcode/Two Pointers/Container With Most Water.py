from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0
        
        while left < right:
            # Calculate the area between the two pointers
            current_area = min(heights[left], heights[right]) * (right - left)
            # Update the maximum area
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the shorter line
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

# Example usage:
solution = Solution()
height1 = [1, 7, 2, 5, 4, 7, 3, 6]
height2 = [2, 2, 2]

print(solution.maxArea(height1))  # Expected output: 36
print(solution.maxArea(height2))  # Expected output: 4