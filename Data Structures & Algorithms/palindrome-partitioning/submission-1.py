class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        path = []
        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        def backtrack(start: int):
            # Base case: reached the end of string
            if start == len(s):
                res.append(path.copy())
                return
            for end in range(start, len(s)):
                # Only proceed if current substring s[start:end+1] is a palindrome
                if is_palindrome(start, end):
                    path.append(s[start : end + 1])
                    backtrack(end + 1)
                    path.pop()  # Backtrack
        backtrack(0)
        return res