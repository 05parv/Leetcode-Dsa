class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        size = len(nums)
        neg = []
        pos = []
        for num in nums:
            if num<0:
                neg.append(num)
            else:
                pos.append(num)

        if len(neg) == 0:
            return [x*x for x in pos]
        if len(pos) == 0:
            res = [x*x for x in neg]
            res.reverse()
            return res

        neg = [x*x for x in neg]
        neg.reverse()
        pos = [x*x for x in pos]

        n = len(neg)
        m = len(pos)
        i = 0
        j = 0
        res =[]

        while i<n and j<m:
            if neg[i]<=pos[j]:
                res.append(neg[i])
                i+=1
            else:
                res.append(pos[j])
                j+=1

        while i<n:
            res.append(neg[i])
            i+=1
        while j<m:
            res.append(pos[j])
            j+=1

        return res