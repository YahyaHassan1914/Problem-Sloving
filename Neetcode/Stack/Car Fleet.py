from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair positions with speeds using zip and then sort by position in descending order
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        
        stack = []  # Stack to store the time it takes each car to reach the target
        
        for p, s in pair:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)  # Start a new fleet
            # If time <= stack[-1], it means this car will join the previous fleet
        
        return len(stack)  # Number of fleets is the size of the stack

# Example usage:
solution = Solution()
target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
print(solution.carFleet(target, position, speed))  # Output: 3
