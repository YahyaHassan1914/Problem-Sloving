from typing import Deque, List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = Deque()  # index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
    
# Example usage
solution = Solution()
print(solution.maxSlidingWindow([1, 3, 2, 4, 1, 9, 10], 3))  # Output: True
print(solution.maxSlidingWindow([1, 3, 2, 6, 3, 7, 9, 4, 1, 9, 10], 5))  # Output: False