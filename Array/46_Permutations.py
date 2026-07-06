class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result =[]
        used =[False]*len(nums)

        def backtrack(curr_path):
            if len(curr_path) == len(nums):
                result.append(curr_path.copy())
                return
            
            for i in range(len(nums)):
                if used[i] :
                    continue

                used[i] =True
                curr_path.append(nums[i])

                backtrack(curr_path)

                used[i] =False
                curr_path.pop()

        backtrack([])

        return result