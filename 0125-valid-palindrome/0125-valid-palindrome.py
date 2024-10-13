class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=""
        for i in s:
            if i.isalnum():
                st+=i.lower()
        p=str(st)
        r=str(st[::-1])
        return p==r