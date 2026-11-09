# Last updated: 11/8/2026, 9:21:38 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        palindrome = str(x)

        if palindrome == palindrome[::-1]:
            return True
        else:
            return False