class Stack:

    def __init__(self):
        self.items = list(())

    def push(self, el):
        self.items.append(el)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
        pass

    def is_empty(self):
        pass



# stack = Stack(("chuj", "cipa"))
# stack.push("kutas")
# print(stack.items)
# stack.pop()
# print(stack.items)
# print (stack.peek())
