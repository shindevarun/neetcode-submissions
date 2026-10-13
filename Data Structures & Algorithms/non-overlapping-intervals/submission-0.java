class Solution {
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
