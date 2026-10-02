class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen = set()

        for idx in nums:
            if idx in seen:
                return True
            seen.add(idx)
        return False