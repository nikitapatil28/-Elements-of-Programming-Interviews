

def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        maxSum=s1=s2=i=j=0
        m, n = len(nums1), len(nums2)
        
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                s1+=nums1[i]
                i+=1
            elif nums1[i] > nums2[j]:
                s2+=nums2[j]
                j+=1
            else:
                maxSum += max(s1,s2)+nums1[i]
                s2=s1=0
                j+=1
                i+=1
        while i <m:
            s1+=nums1[i]
            i+=1
            
        while j < n:
            s2+=nums2[j]
            j+=1
        
        return (max(s1,s2)+maxSum)%1000000007
