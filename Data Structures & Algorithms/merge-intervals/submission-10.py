# first sort the intervals based on the start times. then add the first interval to the res list as default case.
# then for every next interval, check if the start of that interval is less than or equal to end of the last interval in res.
# if it, there is an overlap -> update the end of the last interval in res to be the max of the current end and the new interval's end.
# if no overlap, simply add new interval into res
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        
        intervals.sort()

        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            interval = intervals[i]

            if interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)

        return res