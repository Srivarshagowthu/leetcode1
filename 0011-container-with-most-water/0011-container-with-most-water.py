class Solution:
    def maxArea(self, a: List[int]) -> int:
        l=0
        r=len(a)-1
        maxi=float('-inf')
        while l<r:
            length=min(a[l],a[r])
            bred=r-l
            val=length*bred
            maxi=max(maxi,val)
            if a[l]<a[r]:
                l+=1
            else:
                r-=1
        return maxi