class Solution {

    // want to essentially remove an interval if the start of current interval is less than end of previous interval
    // how to choose which interval to remove? when 2 intervals overlap, you want to remove the interval that ends later
    // because this minimizes the chance of the remaining interval overlapping with the next interval. 
    // We don't have to actuslly physically remove anything from intervals[][] tho. Just keep track of the end val of
    // the previous interval and the start and end of current interval. When we remove interval, just update prevEnd
    // to be the min (interval that ends first) of the previous end and the current end & increment count. If not
    // removing an interval, just set the current end as the previous end
    public int eraseOverlapIntervals(int[][] intervals) {
        int count = 0;
        Arrays.sort(intervals, (a,b) -> Integer.compare(a[0], b[0]));

        int prevEnd = intervals[0][1];

        for(int i = 1; i < intervals.length; i++) {
            int start = intervals[i][0];
            int end = intervals[i][1];

            if(start < prevEnd) {
                count++;
                prevEnd = Math.min(end, prevEnd);
            } else {
                prevEnd = end;
            }
        }

        return count;

    }
}
