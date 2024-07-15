from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Manual sorting (Insertion Sort)
        n = len(nums)
        for i in range(1, n):
            key = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key

        # Remove duplicates from the sorted array in-place
        unique_idx = 0
        for i in range(1, n):
            if nums[i] != nums[unique_idx]:
                unique_idx += 1
                nums[unique_idx] = nums[i]

        max_length = 1
        current_length = 1

        # Linear scan to find the longest consecutive sequence
        for i in range(1, unique_idx + 1):
            if nums[i] == nums[i - 1] + 1:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 1

        return max(max_length, current_length)

# Example usage:
sol = Solution()
print(sol.longestConsecutive([2, 20, 4, 10, 3, 4, 5]))  # Output: 4
print(sol.longestConsecutive([0, 3, 2, 5, 4, 6, 1, 1]))  # Output: 7
