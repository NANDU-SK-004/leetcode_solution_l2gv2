class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash ={}

        for num in nums:
            hash[num] = hash.get(num ,0)+1
        print(hash)