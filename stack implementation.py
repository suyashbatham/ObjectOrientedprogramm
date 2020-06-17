class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def fullStack(self):
        return self.items

stack = Stack()
print("Current stack is",stack.fullStack())
print("Stack is empty",stack.isEmpty())
stack.push(6)
print("Adding element",stack.fullStack())
stack.push(10)
stack.push(11)
stack.push(12)
stack.push(111)
print(stack.fullStack())
stack.pop()
print(stack.fullStack())
print(stack.size())
print(stack.peek())


def checkParenthis(str):
    stack = Stack()
    pushChars,popChars = "<({[", ">)}]"
    for c in str:
        if c in pushChars:
            stack.push(c)
        elif c in popChars:
            if stack.isEmpty():
                return False
            else:
                stackTop = stack.pop()   # pop out first element of stack but last element
                balancingbrackets = pushChars[popChars.index(c)]
                if stackTop != balancingbrackets:
                    return False
        else:
            return False

    return not stack.isEmpty()

print(checkParenthis("()[]"))
