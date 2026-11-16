class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        output = []
        l, r = 0, 0

        while r < len(nums):
            while q and q[-1][0] < nums[r]:
                q.pop()

            q.append((nums[r], r))

            if l > q[0][1]:
                q.popleft()

            if (r + 1) >= k:
                output.append(q[0][0])
                l += 1

            r += 1

        return output
