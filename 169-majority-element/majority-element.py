class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        max_freq = 0
        ans = 0

        for key, value in hashmap.items():
            if value > max_freq:
                max_freq = value
                ans = key

        return ans