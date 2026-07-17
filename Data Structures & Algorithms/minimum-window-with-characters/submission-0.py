class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # Frequency map for every character in t
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        # This will track the frequency of characters currently inside the sldiing window over s
        window = {}

        # Number of unique characters in t that must be satisfies
        need = len(t_count)

        # Number of unique characters whose character count is currently satisfied in the window
        have = 0

        # res stores [left, right] indices of the window. res_len tracks its length. 
        res, res_len = [-1, -1], float("inf")
        left = 0 

        # Phase 1: Expanding the window
        for right in range(len(s)):
            # Move right across s one character at a time adding each new character into the window map
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # If the current character is in t and its count matches the required count in t
            if char in t_count and window[char] == t_count[char]:
                have += 1

            # Phase 2: Shrinking the window from the left
            while have == need:
                # Before shrinking, check if the current window is the smallest valid one found so far, if so record
                if(right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # Shrink the window by removing one character from left, and move left pointer
                left_char = s[left]
                window[left_char] -= 1

                # If removing this character caused its coount to drop below the required amount, then the window is no longer valid for that character, decrement have
                # This will cause the while loop to exit(because have != need now), and for loop resumes expanding right again
                if left_char in t_count and window[left_char] < t_count[left_char]:
                    have -= 1

                left += 1

        l, r = res
        return s[l:r + 1] if res_len != float("inf") else ""