class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        TwoSum, res = {}, set()
        l = len(nums)
        nums.sort()
        for i in xrange(l - 1):
            for j in xrange(i + 1, l):
                ts = nums[i] + nums[j]
                if (ts) not in TwoSum:
                    TwoSum[ts] = [(i, j), ]
                else:
                    TwoSum[ts].append((i, j))
        print TwoSum
        for i in TwoSum:
            if (target - i) in TwoSum:
                for j in TwoSum[i]:
                    for k in TwoSum[target - i]:
                        if j is k: continue
                        temp = list(j + k)
                        if (len(set(temp)) < 4): continue
                        temp.sort()
                        res.add(tuple([nums[_] for _ in temp]))
        return map(list, res)
