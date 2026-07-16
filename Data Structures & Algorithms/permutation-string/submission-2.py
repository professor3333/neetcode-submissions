class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26 # Target
        s2_count = [0] * 26 # Current window

        for i in range(len(s1)):
            # ord(s1[i]) - ord('a') converts a character into an index from 0 - 25
            # ord function converts the character into ASCII integer value, ord('a') is 97
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
                
        # Slide the window across s2
        l = 0
        # Starts sliding the window from the character immediately after the first window to the end of s2
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # The character at the right pointer enters the window, we increment its count
            r_idx = ord(s2[r]) - ord('a')
            s2_count[r_idx] += 1
            if s1_count[r_idx] == s2_count[r_idx]:
                matches += 1
            elif s1_count[r_idx] + 1 == s2_count[r_idx]:
                matches -= 1

            # The character at the left pointer leaves the window, we decrement its count
            l_idx = ord(s2[l]) - ord('a')
            s2_count[l_idx] -= 1
            if s1_count[l_idx] == s2_count[l_idx]:
                matches += 1
            elif s1_count[l_idx] - 1 == s2_count[l_idx]:
                matches -= 1
                
            # Move the left pointer forwad
            l += 1
        
        # Chek the very last window position
        return matches == 26