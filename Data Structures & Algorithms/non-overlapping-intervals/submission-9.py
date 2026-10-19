class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        removed = 0
        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            currStart = intervals[i][0]
            currEnd = intervals[i][1]

            if currStart < prevEnd:
                removed += 1
                prevEnd = min(prevEnd, currEnd)
            else:
                prevEnd = currEnd

        return removed

