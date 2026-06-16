class Solution:
    def jump(self, nums):
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps
'''so this is something like you need to know how many jumps you need
to do to reach the end and fartheast is the index + the value 
and if i reacges the current end you need to jump so jump +=1'''