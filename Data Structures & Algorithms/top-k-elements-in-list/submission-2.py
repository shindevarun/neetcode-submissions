# classic heap problem. First create freq map. Then maintain a min-heap where nodes are (freq of val, val).
# anytime the length of the heap exceeds k, pop from heap. This way the heap will always maintain at most k elements.
# since you pop everytime you have more than k elements and this is a min heap, you always pop smallest freq which means
# you always maintain the maxFreq values in the heap
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