# @leet start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        newNums = nums
        for x in range(0, len(nums)):
            middle = int(len(newNums) / 2)
            
            if target == newNums[middle]:
                return nums.index(target)
            elif target > newNums[middle]:
                newNums = newNums[middle:]
            else:
                newNums = newNums[:middle]
        return -1

        # if target in nums:
        #     return nums.index(target)
        # else:
        #     return -1
# @leet end
