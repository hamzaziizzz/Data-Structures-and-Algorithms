class StackNode:
    def __init__(self, element, bottom=None):
        self.value = element
        self.bottom = bottom


class Stack:
    def __init__(self, top=None):
        self.top = top

    def isEmpty(self):
        if self.top is None:
            return True
        return False

    def push(self, element):
        new_node = StackNode(element)
        if self.isEmpty():
            self.top = new_node
        else:
            new_node.bottom = self.top
            self.top = new_node

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is Empty!")
        else:
            pop_node = self.top
            self.top = pop_node.bottom
            pop_node = None

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is Empty!")
        return self.top.value


def infix_to_prefix(expression: str):
    stack = Stack()

    operators = {'^', '/', '*', '+', '-', '(', ')'}

    precedence = {'^': 3, '/': 2, '*': 2, '+': 1, '-': 1}

    associativity = {
        '/': "left-to-right",
        '*': "left-to-right",
        '+': "left-to-right",
        '-': "left-to-right"
    }

    expression = "".join(expression.split())
    prefix_expression = ''

    for symbol in expression[::-1]:
        if symbol in operators:
            if symbol == ')':
                stack.push(symbol)
            elif symbol == '(':
                while stack.peek() != ')':
                    prefix_expression += stack.peek()
                    stack.pop()
                if stack.peek() == ')':
                    stack.pop()
            else:
                if stack.isEmpty() or stack.peek() == ')':
                    stack.push(symbol)
                elif precedence[symbol] > precedence[stack.peek()]:
                    stack.push(symbol)
                elif precedence[symbol] <= precedence[stack.peek()]:
                    while (stack.isEmpty() is False) and (precedence[symbol] < precedence[stack.peek()]):
                        prefix_expression += stack.peek()
                        stack.pop()
                    if stack.isEmpty():
                        stack.push(symbol)
                    elif precedence[symbol] == precedence[stack.peek()]:
                        if associativity[symbol] == "left-to-right":
                            stack.push(symbol)
                        elif associativity[symbol] == "right-to-left":
                            prefix_expression += stack.peek()
                            stack.pop()
                            stack.push(symbol)
        else:
            prefix_expression += symbol

    while stack.isEmpty() is False:
        prefix_expression += stack.peek()
        stack.pop()

    return prefix_expression[::-1]


if __name__ == "__main__":
    expression = input("Enter the infix expression to be converted into postfix expression: \n")
    prefix_expression = infix_to_prefix(expression)
    print(f"\nPrefix expression of [ {expression} ] is as follows:")
    print(prefix_expression)
