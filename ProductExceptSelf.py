class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_list = []
        total_prod = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                total_prod = num * total_prod
            else:
                zero_count = zero_count + 1

        for num in nums:
            if zero_count == 1:
                if num == 0:
                    num_list.append(total_prod)
                else:
                    num_list.append(0)
                continue
                
            if zero_count >= 2:
                num_list.append(0)

            else:
                new_prod = total_prod/num
                num_list.append(int(new_prod))

        return num_list
        
            

 

