class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash ={}

        for num in nums:
            hash[num] = hash.get(num ,0)+1
        for k in hash.values():
            if k >1:
                return True
        return False