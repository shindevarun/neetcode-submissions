class MinStack {
    Stack<Integer> s;
    Stack<Integer> minStack;

    public MinStack() {
        s = new Stack<>();
        minStack = new Stack<>();
        
    }
    
    public void push(int val) {
        s.push(val);
        
        if(minStack.empty()) {
            minStack.push(val);
        } else {
            if(val < minStack.peek()) {
                minStack.push(val);
            } else {
                minStack.push(minStack.peek());
            }
        }

    }
    
    public void pop() {
        s.pop();
        minStack.pop();
        
    }
    
    public int top() {
        return s.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
