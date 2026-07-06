class Solution(object):
    def shipWithinDays(self, weights, days):
    
        if not weights:
            return 0
        def canShip(capacity):
            wt =0
            day =1
            for w in weights:

                if w >capacity :
                    return False
                if wt+w > capacity:
                    day +=1
                    wt =w
                else:
                    wt +=w
            return day <= days


        low =max(weights)
        high =sum(weights)
        while low <high:
            mid = low +(high -low)//2
            if canShip(mid):
                high =mid 
            else:
                low = mid + 1
        return low

        