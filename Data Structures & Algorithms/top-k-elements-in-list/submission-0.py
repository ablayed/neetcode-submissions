class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            count[i]= count.get(i,0)+1
        return (sorted(count, key=lambda i:count[i], reverse=True)[:k])

            
        