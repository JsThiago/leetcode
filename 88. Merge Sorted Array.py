# Tempo: O(n) Espaço: O(n)
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        c2 = 0
        c1 = 0
        numsAux = nums1[:m]
        for i in range(0,m+n):
            if(i>=min(m,n) and c1 < m and c2 < n and nums2[c2] > numsAux[c1]):
                nums1[i] = numsAux[c1]
                c1 = c1+1
                continue
            if(i>=min(m,n) and c2<n):
                nums1[i] = nums2[c2]
                c2 = c2+1
                continue
            if(i>=min(m,n) and c1<m):
                nums1[i] = numsAux[c1]
                c1 = c1+1
                continue
            if(numsAux[c1]>nums2[c2]):
                
                nums1[i] = nums2[c2]
                c2 = c2+1
                continue
            else:
                nums1[i] = numsAux[c1] 
                c1 = c1 + 1


solution = Solution()
nums1 = [0,0,0,0,0]
solution.merge(nums1,0,[1,2,3,4,5],5)
print(nums1)