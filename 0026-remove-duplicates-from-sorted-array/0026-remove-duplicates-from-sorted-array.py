class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        # Initialize the pointer for the next unique element
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        
        return j

# Example usage:
solution = Solution()
nums1 = [1, 1, 2]
print(solution.removeDuplicates(nums1))

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(solution.removeDuplicates(nums2))
