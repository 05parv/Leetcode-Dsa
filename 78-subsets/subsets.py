class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        total_subsets=1<<n
        res=[]
        for num in range (0,total_subsets):
            st = []
            for i in range (0,n):
                if num & (1<<i) != 0:
                    st.append(nums[i])
            res.append(st)
        return res