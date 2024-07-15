from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        for num in nums:
            if num in seen:
                return True
            seen.append(num)
        return False

# Example usage:
solution = Solution()

# Example 1
nums1 = [1, 2, 3, 3]
print(solution.hasDuplicate(nums1))  # Output: True

# Example 2
nums2 = [1, 2, 3, 4]
print(solution.hasDuplicate(nums2))  # Output: False