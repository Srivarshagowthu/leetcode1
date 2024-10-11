class Solution:
    def isHappy(self, n: int) -> bool:
        def rec(n,l):
            if n==1:
                return True
            if n in l:
                return False
            l.add(n)
            p=str(n)
            s=0
            for i in p:
                s+=(int(i)**2)
            return rec(s,l)
        return rec(n,set())
        