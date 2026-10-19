class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []

        for point in points:
            dist = math.dist(point, [0,0])
            dists.append((dist, point))

        heapq.heapify(dists)

        res = []
        for i in range(k):
            dist, point = heapq.heappop(dists)
            res.append(point)

        return res
        