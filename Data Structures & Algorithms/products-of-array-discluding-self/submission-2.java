class Solution {
    // Key to solving in linear time is to use a prefix and suffix sum array.
    // prefix sum will give you the product of every value before current in array
    // suffix sum will give you the product of every value after current in array
    // once these two are computed, simple iterate through the array and multiply
    // corresponding indices in both prefix and suffix sum arrays
    // - small note: first val of prefix sum and last val of suffix sum are 1 b/c 
    // they are the borders of the array
    public int[] productExceptSelf(int[] nums) {
        int[] prefixArray = new int[nums.length];
        int[] suffixArray = new int[nums.length];
        int[] res = new int[nums.length];

        // hard code first val of prefix and last val of suffix to be 1
        prefixArray[0] = 1;
        suffixArray[nums.length - 1] = 1;

        // populate the prefix product array
        for(int i = 1; i < nums.length; i++) {
            prefixArray[i] = prefixArray[i-1] * nums[i-1];
        }

        // populate the suffix array
        for(int i = nums.length - 2; i >= 0; i--) {
            suffixArray[i] = suffixArray[i+1] * nums[i+1];
        }

        // populate final resultant array
        for(int i = 0; i < nums.length; i++) {
            res[i] = prefixArray[i] * suffixArray[i];
        }

        return res;

    }
}  
