class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Checks whether the input string is empty 
        if not digits:
            return []
        # It creates a dictionary. It maps each digit to the letters associated with that digit on a phone keypad
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []
        path = [] # stores the current combination being built
        # This function recursively builds combinatios. index represents the current digit we are processing
        def backtrack(index: int):
            # Base case) It checks whether we have processed all digits
            if index == len(digits):
                # If the combination is complete, we join the characters in path into a string and add it to res
                res.append("".join(path))
                return
            # This gets the letters corresponding to the current digit. digits[index] gets the current digit
            letters = phone_map[digits[index]]
            # This loops through each possible letter for the current digit
            for char in letters:
                # We choose the current letter. We add it to the current combination
                path.append(char)
                # Now we recursively process the next digit
                backtrack(index + 1)
                # After the recursive call finishes, we remove the last character from path to try other possibilites. This is the backtracking step. 
                path.pop()

        backtrack(0) # This starts the backtracking process
        return res # This contains all complete letter combinations
                
