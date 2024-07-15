from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array
        result = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # Step 4: Skip duplicate elements
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # Skip duplicates for the second element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # Skip duplicates for the third element
                    left += 1
                    right -= 1
        
        return result

# Example usage:
solution = Solution()
nums1 = [-1, 0, 1, 2, -1, -4]
nums2 = [0, 1, 1]
nums3 = [0, 0, 0]

print(solution.threeSum(nums1))  # Expected output: [[-1, -1, 2], [-1, 0, 1]]
print(solution.threeSum(nums2))  # Expected output: []
print(solution.threeSum(nums3))  # Expected output: [[0, 0, 0]]
