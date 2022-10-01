class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
#

class Queue:
    def __init__(self,value):
        newnode = Node(value)
        self.first = newnode
        self.last = newnode
        self.length = 1

    def print(self):
        temp = self.first
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()
    def enqueue(self,newval):
        new_node = Node(newval)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        if self.first is None:
            return None
        temp = self.last
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None

        self.length -= 1
        return temp


my_quoue = Queue(4)
my_quoue.print()
my_quoue.enqueue(2)
my_quoue.print()
my_quoue.dequeue()
my_quoue.print()
my_quoue.dequeue()
my_quoue.print()


