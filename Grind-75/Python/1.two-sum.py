# @leet start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # length = len(nums)
        # for x in range(0, length):
        #     for y in range(x + 1, length):
        #         if nums[x] + nums[y] == target:
        #             return [x, y]
        length = len(nums)
        diffList = []
        for x in range(0, length):
            diff = target - nums[x]
            if nums[x] in diffList:
                return (x, nums.index(diff))
            else:
                diffList.append(diff)
# @leet end
