class Solution:
    def isPalindrome(self, x: int) -> bool:
        palindrome = str(x)

        if palindrome == palindrome[::-1]:
            return True
        else:
            return False