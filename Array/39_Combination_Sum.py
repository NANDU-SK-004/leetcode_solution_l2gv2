class Solution:
    def combinationSum(self, candidates, target):
        final =[] 
        subset =[]
        candidates.sort()
        def solve(index ,subset  ,target):

            if target == 0:
                final.append(subset.copy())
                return
            
            for i in range (index ,len(candidates)):
                if candidates[i] >target :
                    break
                subset.append(candidates[i])
                sum =target-  candidates[i] 
                solve(i ,subset ,sum)
                subset.pop()
                
        solve(0 ,subset,target)
        return final

