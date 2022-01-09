'''
Stack is the data structure where element are represented as stack 
where last inserted element is first to comeout which is also called as LIFO
So, let's implement stack using python as a programming language 
'''


class Stack:

    def __init_(self):
        self.values = list()

    def push(self, element):
        return self.values.append(element)

    def is_Empty(self):
        return len(self.values) == 0

    def pop(self, element):
        if not(self.is_Empty()):
            self.values.pop()
        else:
            print("Stack Underflow")
            return None

    def Top(self):
        if not(self.is_Empty()):
            return self.values[-1]
        else:
            print("Stack Empty")
            return None

    def size(self):
        return len(self.values)


if __name__ == "__main__":
    stack = Stack()
    stack.push("1")
    stack.push("2")
    stack.push("3")
    print(stack.size())
