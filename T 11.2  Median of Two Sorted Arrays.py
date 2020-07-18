# link: https://leetcode.com/problems/median-of-two-sorted-arrays/
# https://www.youtube.com/watch?v=LPFhl65R7ww&t=658s
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        x = len(nums1)
        y = len(nums2)
        if y < x:
            # reverse num1 and num2
            return self.findMedianSortedArrays(nums2, nums1)
        start = 0
        end = x
        while start <= end:
            px = (start + end) // 2
            py = (x + y + 1) // 2 - px
            max_left_x = float('-inf') if px == 0 else nums1[px-1]
            min_right_x = float('inf') if px == x else nums1[px]
            max_left_y = float('-inf') if py == 0 else nums2[py-1]
            min_right_y = float('inf') if py == y else nums2[py]
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (x + y) % 2 == 0:
                    # total len is even
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2.0
                else:
                    # total len is odd
                    return max(max_left_x, max_left_y)
            elif max_left_x > min_right_y:
                end -= 1
            else:
                start += 1
