from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i] +=1
        sorted_dict = sorted(map.items(),key=lambda x:x[1],reverse=True)
        return sorted_dict[0][0]
        

test_data = [2,2,1,1,1,2,2]
solution = Solution()
result = solution.majorityElement(test_data)
print(result)


