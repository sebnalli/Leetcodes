class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        p = []
        pairs = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                p.append(ch)
            
            if ch == ')' or ch == '}' or ch == ']':
                if p and p[-1] == pairs[ch]:
                    p.pop()
                else: 
                    return False

        if not p:
            return True
        else:
            return False






            
        