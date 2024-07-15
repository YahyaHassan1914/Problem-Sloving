from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[nums[i]] = i
        
        # If no solution found
        return []

# Example usage:
solution = Solution()

# Example 1
# nums1 = [3, 4, 5, 6]
# target1 = 7
# print(solution.twoSum(nums1, target1))  # Output: [0, 1]

# Example 2
nums2 = [4, 5, 6]
target2 = 10
print(solution.twoSum(nums2, target2))  # Output: [0, 2]





# from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for x in nums:
#             if x >= target:
#                 continue
#             for y in nums:
#                 if x == y:
#                     continue
#                 if (x+y) == target:
#                     return [nums.index(x), nums.index(y)]
                
# sol= Solution().twoSum(nums = [3,4,5,6], target = 7)
# print(sol)