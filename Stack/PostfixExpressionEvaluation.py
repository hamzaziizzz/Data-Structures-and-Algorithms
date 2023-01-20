def isConstant(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def isVariable(symbol):
    operators = {'[', ']', '{', '}', '(', ')', '%', '/', '*', '+', '-', '^'}
    if (symbol in operators) or (isConstant(symbol) is True):
        return False
    return True


def infix_to_postfix(expression: str):
    stack = []

    expression = list(expression.split(' '))
    for i, operand in enumerate(expression):
        if isConstant(operand) is True:
            expression[i] = float(operand)
        elif isVariable(operand) is True:
            value = float(input(f"Enter value for variable {operand}: "))
            expression[i] = value

    operators = {'^', '/', '*', '+', '-', '(', ')', '{', '}', '[', ']', '%'}

    precedence = {'^': 3, '/': 2, '*': 2, '+': 1, '-': 1}

    associativity = {
        '/': "left-to-right",
        '*': "left-to-right",
        '+': "left-to-right",
        '-': "left-to-right"
    }

    postfix_expression = []
    for symbol in expression:
        if symbol in operators:
            if symbol == '(':
                stack.append(symbol)
            elif symbol == ')':
                while stack[-1] != '(':
                    postfix_expression.append(stack[-1])
                    stack.pop()
                if stack[-1] == '(':
                    stack.pop()
            else:
                if len(stack) == 0 or stack[-1] == '(':
                    stack.append(symbol)
                elif precedence[symbol] > precedence[stack[-1]]:
                    stack.append(symbol)
                elif precedence[symbol] <= precedence[stack[-1]]:
                    while (len(stack) != 0) and (precedence[stack[-1]] > precedence[symbol]):
                        postfix_expression.append(stack[-1])
                        stack.pop()
                    if len(stack) == 0:
                        stack.append(symbol)
                    elif precedence[symbol] == precedence[stack[-1]]:
                        if associativity[symbol] == "right-to-left":
                            stack.append(symbol)
                        elif associativity[symbol] == "left-to-right":
                            postfix_expression.append(stack[-1])
                            stack.pop()
                            stack.append(symbol)
        else:
            postfix_expression.append(symbol)

    while len(stack) != 0:
        postfix_expression.append(stack[-1])
        stack.pop()

    return postfix_expression


def evaluation(expression: list):
    stack = []

    operators = {'^', '/', '*', '+', '-', '(', ')', '{', '}', '[', ']', '%'}

    for symbol in expression:
        if symbol in operators:
            operand2 = stack[-1]
            stack.pop()
            operand1 = stack[-1]
            stack.pop()
            operator = symbol

            if operator == '^':
                value = operand1 ** operand2
            elif operator == '%':
                value = operand1 % operand2
            elif operator == '/':
                value = operand1 / operand2
            elif operator == '*':
                value = operand1 * operand2
            elif operator == '+':
                value = operand1 + operand2
            elif operator == '-':
                value = operand1 - operand2

            stack.append(value)

        else:
            stack.append(symbol)

    return stack[-1]


if __name__ == "__main__":
    print("\nOperator and Operand should be seperated by a space.".upper())
    expression = input("Enter the expression to be evaluated:\n")

    postfix_expression = infix_to_postfix(expression)
    print("\nAfter substituting the given values for the variables, the postfix expression for the above infix expression becomes as follows:")
    for symbol in postfix_expression:
        print(symbol, end='  ')
    print()

    answer = evaluation(postfix_expression)
    print(f"\nFinal value for the expression is {answer}")
