class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}                          # number -> index
        for j in range(len(nums)):
            needed=target-nums[j]
            if needed in seen:
                return [seen[needed], j]
            seen[nums[j]]=j