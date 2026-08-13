
class Solution(object):
    def maximumSubarraySum(self, nums, k):
        window_sum = 0
        max_sum = 0
        count = {}

        for i in range(len(nums)):
            window_sum += nums[i]
            count[nums[i]] = count.get(nums[i], 0) + 1

            if i >= k:
                window_sum -= nums[i-k]
                count[nums[i-k]] -= 1

                if count[nums[i-k]] == 0:
                    del count[nums[i-k]]

            if i >= k - 1 and len(count) == k:
                max_sum = max(max_sum, window_sum)

        return max_sum