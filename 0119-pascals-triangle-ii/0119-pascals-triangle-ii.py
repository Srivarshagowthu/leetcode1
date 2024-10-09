import math
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        fin=[[1]]
        for i in range(1,34):
            res=[]
            for j in range(i+1):
                res.append(math.comb(i,j))
            fin.append(res)
        return fin[rowIndex]
        