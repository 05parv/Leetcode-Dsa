class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if k==0:
            return nums
        rotate = n%k

        for i in range (0,k):
            e=nums.pop()
            nums.insert(0,e)
        