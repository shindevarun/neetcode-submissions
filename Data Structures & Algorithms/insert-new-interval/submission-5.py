class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # case 1: end of the newInterval is less than the beginning of the current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # case 2: beginning of the newInterval is greater than the end of current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # case 3: newInterval overlaps with current interval
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                # dont add just yet since this can now overlap with the next interval

        res.append(newInterval)
        return res