class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.insert(0,float("-infinity"))
        nums1.append(float("infinity"))
        nums2.insert(0,float("-infinity"))
        nums2.append(float("infinity"))
        
        length = len(nums1) + len(nums2)
        total = (length + 1)//2
        
        start = max(0, total - len(nums2) - 1)
        end = min(total - 1, len(nums1) - 1)
        
        curr = int(end + start)//2

        am0, bm0 = nums1[curr], nums2[total - curr - 2]
        am1, bm1 = nums1[curr + 1], nums2[total - curr - 1]
        

        while(am0 > bm1 or am1 < bm0):
            if am0 > bm1:
                end = curr
                
            if am1 < bm0:
                start = curr
                
            curr = int(end + start)//2
            
            am0, bm0 = nums1[curr], nums2[total - curr - 2]
            am1, bm1 = nums1[curr + 1], nums2[total - curr - 1] 
            
        if length % 2 == 0:
            return float(max(am0, bm0) + min(am1,bm1))/2
        
        return max(am0, bm0)
