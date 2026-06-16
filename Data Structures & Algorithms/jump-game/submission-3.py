class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0
        #this is by tracing back can i reach the goal,
        # in the first goal will be the last index,later on
        #the goal changes to the prev index of where the jump came from