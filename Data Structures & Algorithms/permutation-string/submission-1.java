class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int left = 0;
        int right = s1.length();
        char[] s1Arr = s1.toCharArray();
        Arrays.sort(s1Arr);

        while(right <= s2.length()) {
            String s2Builder = "";
            for(int i = left; i < right; i++) {
                s2Builder = s2Builder + s2.charAt(i);
            }
            
            char[] s2Arr = s2Builder.toCharArray();
            Arrays.sort(s2Arr);

            left++;
            right++;

            // System.out.println(Arrays.toString(s1Arr) + ", " + Arrays.toString(s2Arr));
        

            if(Arrays.equals(s1Arr, s2Arr)) {
                return true;
            }
        }

        return false;
        
    }
}
