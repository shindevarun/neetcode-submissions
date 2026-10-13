class Solution {
    // o(log(n*m)) solution where n is number or rows and m is number of columns.
    // essentially treating the 2d matrix as one long array. same as regular b.s.
    // but only difference is how to calculate actual index of value (midpoint).
    // turns out if you take the regular mid ([left + right] / 2) and then take
    // mid / numCols, you get the row index. when you do mid % numCols, you get
    // column index. now you can use matrix[row][col] as you actual midpoint to 
    // use in b.s. and continue as you normally would

    // other approach where you do b.s. on the rows by checking first and last vals
    // and then b.s. on the one row that could possibly contain target has a time
    // complexity of log(n) + log(m). The implemented algorithm has a complexity
    // of log(n*m) which actually equals log(n) + log(m) so both these algorithms
    // have the same time complexity.
    public boolean searchMatrix(int[][] matrix, int target) {
        int left = 0;
        int right = matrix[0].length * matrix.length - 1;

        while (left <= right) {
            int mid = (left  + right) / 2;

            int row = mid / matrix[0].length;
            int col = mid % matrix[0].length;

            if(matrix[row][col] == target) {
                return true;
            } else if (matrix[row][col] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return false;

    }
}
