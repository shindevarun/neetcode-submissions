class Solution {
    public int maxArea(int[] heights) {

        // working n^2 brute force solution
        // int maxVolume = 0;

        // for(int i = 0; i < heights.length; i++) {
        //     for(int j = i + 1; j < heights.length; j++) {
        //         int left = heights[i];
        //         int right = heights[j];

        //         int max = 0;
        //         if(right > left) {
        //             max = left;
        //         } else {
        //             max = right;
        //         }


        //         int volume = max * (j - i);
        //         if(volume > maxVolume) {
        //             maxVolume = volume;
        //         }
        //     }
        // }

        // return maxVolume;


        int maxVolume = 0;

        int left = 0;
        int right = heights.length - 1;

        while(left < right) {
            int max = 0;
            int leftHeight = heights[left];
            int rightHeight = heights[right];

            if(rightHeight > leftHeight) {
                max = leftHeight;
            } else {
                max = rightHeight;
            }

            int volume = max * (right - left);
            if(volume > maxVolume) {
                maxVolume = volume;
            }

            if(rightHeight > leftHeight) {
                left++;
            } else {
                right--;
            }
        }

        return maxVolume;
    }
}
