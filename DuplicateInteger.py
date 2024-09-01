class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_map = {}
        for num in nums:
            if num in nums_map:
                nums_map[num] = nums_map[num] + 1
                if nums_map[num] == 2:
                    return True
            else:
                nums_map[num] = 1
        return False