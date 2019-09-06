# https://leetcode.com/problems/merge-sorted-array/
# runtime beats 61.12%
# memory usage beats 58.97%

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i, j in enumerate(range(m, len(nums1))):
            nums1[j] = nums2[i]
            
        for i, num in enumerate(sorted(nums1)):
            nums1[i] = num
