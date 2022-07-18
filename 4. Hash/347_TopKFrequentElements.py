class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = []
        for i in nums:
            try:
                count[i] += 1
            except:
                count[i] = 1
        print(count)
        
        for _ in range(k):
            topK = max(count, key=count.get)
            ans.append(topK)
            del count[topK]
        
        return ans