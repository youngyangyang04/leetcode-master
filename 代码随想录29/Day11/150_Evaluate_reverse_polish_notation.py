class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []  # Initialize an empty stack

        for i in range(len(tokens)):  # Use 'range' to iterate through indices
            if tokens[i] in {
                "+",
                "-",
                "*",
                "/",
            }:  # Check if the current token is an operator
                num2 = st.pop()  # Pop the top operand from the stack
                num1 = st.pop()  # Pop the second operand from the stack

                if tokens[i] == "+":
                    st.append(num1 + num2)
                elif tokens[i] == "-":
                    st.append(num1 - num2)
                elif tokens[i] == "*":
                    st.append(num1 * num2)
                elif tokens[i] == "/":
                    # Handle division by zero
                    st.append(int(num1 / num2))
            else:
                st.append(
                    int(tokens[i])
                )  # Convert the token to an integer and push it onto the stack

        return st.pop()  # The final result is the only element left in the stack
