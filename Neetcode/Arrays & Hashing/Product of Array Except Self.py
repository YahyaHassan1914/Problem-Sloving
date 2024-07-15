from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for x in range(len(nums)):
            sum = 1
            for y in range(len(nums)):
                if x == y:
                    continue

                sum = sum * nums[y]
            res.append(sum)
        
        return res

# Example usage
solution = Solution()
print(solution.productExceptSelf([1, 2, 4, 6]))  # Output: [48, 24, 12, 8]
print(solution.productExceptSelf([-1, 0, 1, 2, 3]))  # Output: [0, -6, 0, 0, 0]