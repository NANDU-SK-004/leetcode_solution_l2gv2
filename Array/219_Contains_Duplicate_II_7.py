class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash ={}
        for num in nums:
            hash[num] = hash.get(num ,0)+1
        arr =[]


        for key ,value in hash.items():
            if value >1:
                arr.append(key) 

        for val in arr:
            if k >= len(nums):
                if nums.count(val) > 1:
                    return True
            else:
                for i in range(len(nums)-k +1):
                    
                    if nums[i:i+k+1].count(val) > 1:
                        return True
        return False



        