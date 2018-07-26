"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        nonzero_end = m
        while i < nonzero_end and j < n:
            if nums2[j] < nums1[i]:
                nums1[i:] = [nums2[j]] + nums1[i:nonzero_end]
                nonzero_end += 1
                j += 1
            else:
                i += 1
        # assign rest of nums2 to nums1 tail
        if j < n:
            nums1[nonzero_end:] = nums2[j:]
            nonzero_end += n-j
        return