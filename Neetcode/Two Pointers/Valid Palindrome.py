class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Remove non-alphanumeric characters and convert to lowercase
        clean_s = [c.lower() for c in s if c.isalnum()]
        
        # Step 2: Use two pointers to check if the string is a palindrome
        left, right = 0, len(clean_s) - 1
        while left < right:
            if clean_s[left] != clean_s[right]:
                return False
            left += 1
            right -= 1
        
        return True

# Example usage:
sol = Solution()
print(sol.isPalindrome("Was it a car or a cat I saw?"))  # Output: True
print(sol.isPalindrome("tab a cat"))  # Output: False
