class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
       
        high = len(nums)-1

        while low<=high:
            mid = int((low+high) / 2)
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                high = mid - 1
                continue
            if target > nums[mid]:
                low = mid + 1
                continue
        return -1
