class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> s = new Stack<>();

        for(int i = 0; i < tokens.length; i++) {
            String token = tokens[i];
            System.out.println(s);

            if(!token.equals("+") && !token.equals("-") && !token.equals("*") && !token.equals("/")) {
                s.push(Integer.parseInt(token));
            } else {
                // int second = Integer.parseInt(s.pop());
                // int first = Integer.parseInt(s.pop());
                int second = s.pop();
                int first = s.pop();

                if (token.equals("+")) {
                    s.push(first + second);
                } else if (token.equals("-")) {
                    s.push(first - second);
                } else if (token.equals("*")) {
                    s.push(first * second);
                } else if (token.equals("/")) {
                    s.push(first / second);
                }
            }
        }

        return s.peek();
    }
}
