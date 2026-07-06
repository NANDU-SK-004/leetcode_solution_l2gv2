class Solution {
public:
    int maxArea(vector<int>& height) {
    
        int max_ar = INT_MIN;
        int n= height.size();
        int st=0 ,end =n-1;
        while(st<end){
            int diff= end - st;
            int m =min(height[st] ,height[end]);
            int ar=m*diff;
            max_ar=max(ar,max_ar);
            
            height[st] < height[end] ? st++ :end --;
        }
        return max_ar;
    }
       
    
};