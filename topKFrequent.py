class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        top_nums = []
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        sorted_nums = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            top_nums.append(sorted_nums[i][0])
        return top_nums