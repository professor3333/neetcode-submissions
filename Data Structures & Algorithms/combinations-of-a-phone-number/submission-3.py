class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        # It creates a dictionary. It maps each digit to the letters associated with that digit on a phone keypad
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []
        path = []

        def backtrack(index: int):
            if index == len(digits):
                res.append("".join(path))
                return

            letters = phone_map[digits[index]]
            for char in letters:
                path.append(char)
                backtrack(index + 1)
                path.pop() 
        backtrack(0)
        return res