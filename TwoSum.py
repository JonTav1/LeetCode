class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numMap = {}
        length = len(nums)
        for i in range(length):#make a hashmap of the values
            numMap[nums[i]] = i
        
        for i in range(length):
            difference = target - nums[i]#for every value in the nums list, subtract it and see what value we need
            if difference in numMap and numMap[difference] != i:#if we find the value that makes the target true, return it.
                return [i, numMap[difference]]

        return []