class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp=[]
        n=len(nums)
        for i in range (0,n):
            if nums[i]!=0:
                temp.append(nums[i])
            m=len(temp)
        for i in range (0,m):
            nums[i]=temp[i]
        for i in range (m,n):
            nums[i]=0


        