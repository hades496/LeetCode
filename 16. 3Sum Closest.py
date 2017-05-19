class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0x7fffffff
        nums.sort()
        if target < 0:
            for i in xrange(len(nums)):
                left, right = i + 1, len(nums) - 1
                while left < right:
                    sum = nums[i] + nums[left] + nums[right]
                    if abs(sum - target) < abs(res - target): res = sum
                    if (sum > target):
                        right -= 1
                    elif (sum < target):
                        left += 1
                    else:
                        return res
        else:
            nums = nums[::-1]
            for i in xrange(len(nums)):
                left, right = i + 1, len(nums) - 1
                while left < right:
                    sum = nums[i] + nums[left] + nums[right]
                    if abs(sum - target) < abs(res - target): res = sum
                    if (sum < target):
                        right -= 1
                    elif (sum > target):
                        left += 1
                    else:
                        return res
        return res
