class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = "".join(char.lower() for char in s if char.isalnum())
        return cleaned_string == cleaned_string[::-1]