class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = [] # Stores the current partition being built
        # Checks whether a substring of s is a palindrome. left is the starting index of the substring, right is the ending index of the substring
        def is_palindrome(left: int, right: int) -> bool:
            # Compare character from both ends of the strings, continues while the left pointer is less than the right
            while left < right:
                # If this case is true, the substring cannot be a palindrome, return false immediately
                if s[left] != s[right]:
                    return False
                # This lets us choose the next pair of characters by moving both pointers one step
                left += 1 # One step right
                right -= 1 # One step left
            # If the loop finishes without finding mismatched characters, then the substring is a palindrome. Single-character substrings automatically return True
            return True
        # This function recursively build valid partitions. start is the index where we need to partition the remaining part of the string. 
        def backtrack(start: int):
            # Base case) Checks whether we have reached the end of the string. If this is true(start == len(s)), then every character has been placed into a palindrome substring. That means the current path is a complete valid palindrome
            if start == len(s):
                # Add the current complete partition to res. 
                res.append(path.copy())
                return
            # This loop tries every possible ending index for the next substring. The next substring starts at start and ends at end
            for end in range(start, len(s)):
                # Wheter the substring: s[start: end + 1] is a palindrome
                if is_palindrome(start, end):
                    # If the substring is a palindrome, we add it to the current partition
                    path.append(s[start: end + 1])
                    # Now, we recursively partition the rest of the string. The current substring ends at end, so the next start index is end + 1
                    backtrack(end + 1)
                    # We remove it from path to try the next possible substring
                    path.pop()
        backtrack(0) # This starts the backtracking process
        return res # This contains all valid palindrome partitions