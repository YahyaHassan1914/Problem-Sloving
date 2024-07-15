from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        max_freq = 0
        char_count = defaultdict(int)
        
        for right in range(len(s)):
            char_count[s[right]] += 1
            max_freq = max(max_freq, char_count[s[right]])
            
            # If the current window size minus the frequency of the most frequent character
            # is greater than k, shrink the window
            if (right - left + 1) - max_freq > k:
                char_count[s[left]] -= 1
                left += 1
            
            # Update the maximum length of the valid window
            max_len = max(max_len, right - left + 1)
        
        return max_len

# Example usage
solution = Solution()
print(solution.characterReplacement("XYYX", 2))  # Output: 4
print(solution.characterReplacement("AAABABB", 1))  # Output: 5
