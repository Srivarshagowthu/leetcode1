from collections import Counter
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=[]
        res1=[""]
        for j in range(len(strs[0])):
            p=strs[0][:j+1]
            res.append(p)
        print(sorted(res))
        for k in res:
            c=0
            for i in strs:
                if k == i[:len(k)]:
                    c+=1
            if c==len(strs):
                res1.append(k)
        return res1[-1]
                