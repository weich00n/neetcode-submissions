class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            if token in '+-*/':
                one = stack.pop()
                two = stack.pop()
                if token == '+':
                    stack.append(one + two)
                elif token == '-':
                    stack.append(two - one)
                elif token == '*':
                    stack.append(one * two)
                else:
                    stack.append(int(two / one))
            else:
                stack.append(int(token))
            
        return stack[0]



