class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value):
        first_node = Node(value)
        self.top = first_node
        self.height = 1

    def print(self):
        temp = self.top
        while temp is not None:
            print(temp.value,end=" ")
            temp = temp.next
        print()

    def push(self,newval):
        new_node = Node(newval)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp


my_stack = Stack(0)
my_stack.print()
my_stack.push(1)
my_stack.print()

print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
my_stack.print()