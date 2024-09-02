class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_map = {}
        max_seq = 1
        
        for num in nums:
            if num not in num_map:
                left = num_map.get(num - 1, 0)
                right = num_map.get(num + 1, 0)
                
                current_seq = left + right + 1
                
                max_seq = max(max_seq, current_seq)

                num_map[num] = current_seq
                num_map[num - left] = current_seq
                num_map[num + right] = current_seq
        
        return max_seq

