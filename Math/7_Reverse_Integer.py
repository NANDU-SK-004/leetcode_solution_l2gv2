class Solution(object):
    def reverse(self, x):
        y =str(x)
        j=0
        if y[0] == "-":
            s=y[0]
            j=1
        val=y[-1:-len(y)-1+j:-1]
    
        if j==1:
            val=s+val
    
        final=int(val)

        if final < pow(2 , 31)-1 and final > -pow(2 ,31) :
            return final
        else:
            return 0 