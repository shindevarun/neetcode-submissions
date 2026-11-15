class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = self.createFreqMap(nums)

        heap = []
        for key,v in counts.items():
            heapq.heappush(heap, (v, key))
            
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append((heapq.heappop(heap))[1])

        return res
        
    def createFreqMap(self, nums):
        freq = {}

        for s in nums:
            if s in freq:
                freq[s] = freq[s]+1
            else:
                freq[s] = 1

        return freq