class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;

        boolean found = false;
        int[] retArr = new int[2];

        while(found == false) {
            int sum = numbers[left] + numbers[right];

            if(sum < target) {
                left++;
            } else if (sum > target) {
                right--;
            } else {
                retArr[0] = left + 1;
                retArr[1] = right + 1;
                found = true;
            }
        }

        return retArr;
    }
}
