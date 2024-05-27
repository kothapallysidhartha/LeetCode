class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        if n == 1:
            return nums[0]

        # Initialize variables
        prev_max = 0  # maximum amount that can be robbed from previous houses
        curr_max = 0  # maximum amount that can be robbed including current house

        # Iterate through the houses
        for num in nums:
            # Calculate the new maximum amount that can be robbed including the current house
            temp = curr_max
            curr_max = max(prev_max + num, curr_max)
            prev_max = temp

        # The final result is the maximum amount that can be robbed
        return curr_max
