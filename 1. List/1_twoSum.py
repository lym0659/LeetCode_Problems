class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = []
        for e1 in nums:
            e2 = target - e1      
            tmp = nums.index(e1)
            rest_nums = nums[tmp+1:]
            if e2 in rest_nums:
                index.append(nums.index(e1))
                del nums[nums.index(e1)]                  
                index.append(nums.index(e2)+1)
                break
        return index
                    