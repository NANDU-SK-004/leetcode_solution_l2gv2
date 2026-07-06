# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
#         if len(nums1) > len(nums2):
#             nums1 , nums2 =nums2 ,nums1
#         m,n =len(nums1) ,len(nums2)
#         left ,right =0 ,m 
#         total_left =(m+n+1)//2

#         while left <= right:
#             i = left + (right - left) // 2
#             j =total_left -i

#             l1 =float('-inf')if i==0 else nums1[i-1]
#             l2 =nums2[j]

#             if l1<= r2 and l2<=r1:
#                 if (m+n) %2: ##odd valid
#                     return max(li ,l2)
#                 else :
#                     return (max(l1,l2)+min(r1,r2))//2.0
#             elif l1 >r2:
#                 right =i-1
#             else:
#                 left =i+1
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        left, right = 0, m
        total_left = (m + n + 1) // 2

        while left <= right:

            i = left + (right - left) // 2
            j = total_left - i

            l1 = float('-inf') if i == 0 else nums1[i - 1]
            r1 = float('inf') if i == m else nums1[i]

            l2 = float('-inf') if j == 0 else nums2[j - 1]
            r2 = float('inf') if j == n else nums2[j]

            if l1 <= r2 and l2 <= r1:

                if (m + n) % 2:
                    return max(l1, l2)

                return (max(l1, l2) + min(r1, r2)) / 2

            elif l1 > r2:
                right = i - 1

            else:
                left = i + 1