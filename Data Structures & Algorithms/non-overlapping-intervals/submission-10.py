# no need to actually remove anything
# first sort on start times. then, add the first interval as the baseline.
# then for each interval, see if the start time of that interval is less than the end time of the previous interval, which means overlap.
# in this case, we can increment our count by 1, and change the prevEnd to be the min(prevEnd, currEnd).
# min because we want to keep the interval that has the lesser end time since this is more likely to have lesser overlaps with the subsequent intervals
# if no overlap, just update prevEnd to be currEnd
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

