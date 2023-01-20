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

def infix_to_prefix(expression: str):
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

    prefix_expression = []
    for symbol in expression[::-1]:
        if symbol in operators:
            if symbol == ')':
                stack.append(symbol)
            elif symbol == '(':
                while stack[-1] != ')':
                    prefix_expression.append(stack[-1])
                    stack.pop()
                if stack[-1] == ')':
                    stack.pop()
            else:
                if len(stack) == 0 or stack[-1] == ')':
                    stack.append(symbol)
                elif precedence[symbol] > precedence[stack[-1]]:
                    stack.append(symbol)
                elif precedence[symbol] <= precedence[stack[-1]]:
                    while (len(stack) != 0) and (precedence[stack[-1]] > precedence[symbol]):
                        prefix_expression.append(stack[-1])
                        stack.pop()
                    if len(stack) == 0:
                        stack.append(symbol)
                    elif precedence[symbol] == precedence[stack[-1]]:
                        if associativity[symbol] == "left-to-right":
                            stack.append(symbol)
                        elif associativity[symbol] == "right-to-left":
                            prefix_expression.append(stack[-1])
                            stack.pop()
                            stack.append(symbol)
        else:
            prefix_expression.append(symbol)

    while len(stack) != 0:
        prefix_expression.append(stack[-1])
        stack.pop()

    return prefix_expression[::-1]


def evaluation(expression: list):
    stack = []

    operators = {'^', '/', '*', '+', '-', '(', ')', '{', '}', '[', ']', '%'}

    for symbol in expression[::-1]:
        if symbol in operators:
            operand1 = stack[-1]
            stack.pop()
            operand2 = stack[-1]
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

    prefix_expression = infix_to_prefix(expression)
    print("\nAfter substituting the given values for the variables, the prefix expression for the above infix expression becomes as follows:")
    for symbol in prefix_expression:
        print(symbol, end='  ')
    print()

    answer = evaluation(prefix_expression)
    print(f"\nFinal value for the expression is {answer}")
