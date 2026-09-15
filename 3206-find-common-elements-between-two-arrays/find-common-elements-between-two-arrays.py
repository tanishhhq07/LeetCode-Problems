class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        a = set(nums1) & set(nums2)
        count1 = 0
        count2 = 0
        for i in nums1:
            if i in a:
                count1 += 1
        for j in nums2:
            if j in a:
                count2 += 1
        return [count1,count2]