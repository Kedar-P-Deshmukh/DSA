class Node:
    def __init__(self,value):
        self.value= value
        self.next= None
        self.prev = None


class DoublyLinkedList:
    def __init__(self,value):
        first_node = Node(value)
        self.head = first_node
        self.tail = first_node
        self.lenght = 1

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()

    def append(self,newval):
        newnode = Node(newval)
        if self.head is  None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode
        self.lenght+=1
        return True

    def pop(self):
        if self.head is None:
            return None
        temp=self.tail
        if self.lenght == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.lenght -=1
        return temp

    def prepend(self,newval):
        newnode = Node(newval)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        self.lenght += 1
        return True

    def pop_first(self):
        if self.head is None:
            return None
        temp = self.head
        if self.lenght == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.lenght -= 1
        return temp

    def get(self,index):
        if index<0 or index>=self.lenght:
            return None
        temp= self.head
        if index< self.lenght/2:
            for _ in range(index):
                temp=temp.next
        else:
            temp= self.tail
            for _ in range(self.lenght-1, index,-1):
                temp=temp.prev

        return temp

    def set_value(self,index,newvalue):
        temp=self.get(index)
        if temp:
            temp.value=newvalue
            return True
        return False

    def insert(self,index,newvalue):
        if index<0 or index>self.lenght:
            return False
        if index == 0:
            return self.prepend(newvalue)
        if index == self.lenght:
            return self.append(newvalue)

        before = self.get(index-1)
        after = before.next
        newnode= Node(newvalue)

        newnode.next=after
        newnode.prev=before
        before.next=newnode
        after.prev = newnode

        self.lenght+=1
        return True

    def remove(self,index):
        if index<0 or index>=self.lenght:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.lenght-1:
            return self.pop()
        temp = self.get(index)
        after = temp.next       #temp.next.prev = temp.prev
        before = temp.prev      #temp.prev.next = temp.next

        after.prev= before
        before.next =after

        temp.next=None
        temp.prev=None

        self.lenght-=1
        return temp



my_doubly_linked_list = DoublyLinkedList(0)
# my_doubly_linked_list.print()
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
#
# my_doubly_linked_list.print()
# my_doubly_linked_list.pop()
# my_doubly_linked_list.print()
# my_doubly_linked_list.pop()
# my_doubly_linked_list.print()
# my_doubly_linked_list.pop()
# my_doubly_linked_list.print()
# my_doubly_linked_list.prepend(0)
# my_doubly_linked_list.print()

#
# my_doubly_linked_list.pop_first()
# my_doubly_linked_list.print()
# my_doubly_linked_list.pop_first()
# my_doubly_linked_list.print()
# my_doubly_linked_list.pop_first()
# my_doubly_linked_list.print()
# my_doubly_linked_list.pop_first()
# my_doubly_linked_list.print()
# my_doubly_linked_list.pop_first()
# my_doubly_linked_list.print()

my_doubly_linked_list.append(3)
# print(my_doubly_linked_list.set_value(1,123456))
# my_doubly_linked_list.print()

print(my_doubly_linked_list.remove(3))
my_doubly_linked_list.print()