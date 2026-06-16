class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = nums[0]
        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)
            if current_sum < 0:
                current_sum = 0
        return max_sum
'''here what happens is we take current sum and the max sum
check the max between both then update the max sum 
the current sum is resset to 0 whenever it becomes -ve
cause the negative number will reduce the overall sum of the substring'''