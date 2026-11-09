class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen= set()
        for _ in nums:
            if _  not in seen:
                seen.add(_)
            else:
                return True
        return False


        