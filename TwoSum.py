class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        index_list = []
        for i in range(len(nums)):
            num_map[nums[i]] = i
        for num in nums:
            difference = target - num
            if difference in num_map:
                index_list.append(num_map[num])
                index_list.append(num_map[difference])
                return index_list
        return index_list