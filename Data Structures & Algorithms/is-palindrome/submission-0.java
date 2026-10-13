class Solution {
    public boolean isPalindrome(String s) {
        String s2 = "";
        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if(Character.isLetterOrDigit(c)) {
                s2 += Character.toLowerCase(c);
            }
        }

        int l = 0;
        int r = s2.length() - 1;

        while(l < r) {
            if(s2.charAt(l) == s2.charAt(r)) {
                l++;
                r--;
            } else {
                return false;
            }
        }

        return true;
        
    }
}
