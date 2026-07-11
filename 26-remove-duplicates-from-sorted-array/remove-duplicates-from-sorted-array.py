class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        hash_map={}
        for i in range(0,n):
            hash_map[nums[i]]=0
        j=0
        for k in  hash_map:
            nums[j]=k
            j+=1
        return j