class Solution(object):
    
    def rec(self ,index,nums , result ,ans):
        if index == len(nums):
            ans.append(result[:])
            return

        result.append(nums[index])
        self.rec(index + 1,nums , result ,ans)

        result.pop()

        self .rec(index + 1,nums , result ,ans)

        
    def subsets(self, nums):
        ans =[]
        self.rec(0 ,nums ,[] ,ans)
        return ans
    

        