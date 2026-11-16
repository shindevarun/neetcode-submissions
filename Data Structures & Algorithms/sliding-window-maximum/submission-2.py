# Monotonic Decreasing Queue Problem to make this a O(n) solution.
# Main idea is this:

# You initialize l, r to 0 and you move both l and r one step at a time since this is a fixed size window
# Everytime you move right, you will need to add the new element to a queue, that's for sure.

# But before adding to the queue, you will need to pop everytime from queue that's smaller than this value, then you can add.

# Then next check is if the index value at the front of the queue is less than index of l, meaning that that value is no longer in the window since l has moved past it.
# If that's the case, remove that value.
# This way the queue always holds the values in decreasing order, representing the actual values inside your current window so you can always access the top value in constant time.

# Also important to not only put values into queue, but put tuple of (value, index). So this way you can use that index to compare to l and check if values need to be removed from window.

# Lastly, check if (r+1) >= k, if so add the value from front of queue to output array. This is just for edge case since you initialize right pointer at 0. You don't want to add
# values to output before r is actually at size of a window before the whole window moves. This case also allows you to move l once r is actually at required window size since r
# can move after every iteration of loop but l should move at every iteration of loop only AFTER you have first reached window size.
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        output = []
        l, r = 0, 0

        while r < len(nums):
            # remove all smaller elements than new element from q 
            while q and q[-1][0] < nums[r]:
                q.pop()

            q.append((nums[r], r))

            # if old max value is no longer in the window (l moved past it), remove it
            if l > q[0][1]:
                q.popleft()

            # add the max to output everytime except before r has reached the size of a window intially
            if (r + 1) >= k:
                output.append(q[0][0])
                l += 1

            r += 1

        return output
