class Solution {
    public int maxArea(int[] heights) {
        int maxVolume = 0;

        for(int i = 0; i < heights.length; i++) {
            for(int j = i + 1; j < heights.length; j++) {
                int left = heights[i];
                int right = heights[j];

                int max = 0;
                if(right > left) {
                    max = left;
                } else {
                    max = right;
                }

                

                int volume = max * (j - i);
                if(volume > maxVolume) {
                    maxVolume = volume;
                    // System.out.println(maxVolume);
                }

            }
        }

        return maxVolume;
    }
}
