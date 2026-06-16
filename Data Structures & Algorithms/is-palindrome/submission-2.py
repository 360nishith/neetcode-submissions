class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        s = s.replace(",", "")
        s = s.replace(":", "")
        s = s.replace("?", "")
        s = s.replace(".", "")
        s = s.replace("!", "")
        s = s.replace("'", "")

        return s == s[::-1]