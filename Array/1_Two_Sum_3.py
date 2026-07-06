class Solution(object):
    
    def twoSum(self, nums, target):
        result =[]
        for i in range(len(nums)):
            if (target -nums[i]) in nums and nums.index((target -nums[i])) != i:
                result.append(i)
                result.append(nums.index((target -nums[i])))
                return result
            
