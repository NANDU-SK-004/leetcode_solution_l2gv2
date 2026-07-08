class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash ={}

        # for num in nums:
        #     hash[num] = hash.get(num ,0)+1
        # for k in hash.values():
        #     if k >1:
        #         return True
        # return False

        a =len(nums)
        b = len(set(nums))

        return not a ==b