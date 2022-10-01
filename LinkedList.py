class Node:
    def __init__(self, value):
        self.value=value
        self.next=None


class LinkedList:
    def __init__(self, value):
        first_node=Node(value)
        self.head= first_node
        self.tail= first_node
        self.lenth=1

    def printlist(self):
        temp=self.head
        while temp !=None:
            print(temp.value,end=" ")
            temp =temp.next
        print()
    def append(self,newval):
        newnode = Node(newval)
        if self.head == None:
            self.head= newnode
            self.tail = newnode

        else:
            self.tail.next=newnode
            self.tail=newnode

        self.lenth += 1
        return True

    def pop(self):
        if self.head == None:
            print('List is empty cant pop')
            return None
        elif self.head == self.tail:
            temp=self.head #useful for return     fix needed
            self.head = self.tail =  None
            print('List is empty now')

        else:
            temp = self.head
            while temp.next!= self.tail:
                temp = temp.next
            temp.next= None
            self.tail= temp
        self.lenth-=1
        return temp

    def prepend(self,newval):
        newprenode=Node(newval)
        if self.head == None:
            self.head=self.tail=newprenode
        else:
            newprenode.next=self.head
            self.head=newprenode
        self.lenth+=1
        return True

    def popfirst(self):
        temp = self.head
        if self.head==None:
            print('List is empty cant pop')
            return temp
        elif self.head.next==None:
            self.head=self.tail=None
            print('List is empty now')
        else:
            self.head=self.head.next
        self.lenth_=1
        temp.next=None
        return temp
    def get_value(self,index):
        if index<0 or index>=self.lenth:
            return None
        temp= self.head
        for _ in range(index):
            temp=temp.next
        return temp

    def set_value(self,index,value):
        temp=self.get_value(index)
        if temp:
            temp.value=value
            return True
        return False
    def insert(self,index,newvalue):
        if index<0 or index>self.lenth:
            return False
        elif index==0:
            return self.prepend(newvalue)
        elif index==self.lenth:
            return self.append(newvalue)
        new_node=Node(newvalue)
        temp=self.get_value(index-1)
        new_node.next=temp.next
        temp.next=new_node
        self.lenth+=1
        return True

    def remove(self,index):
        if index<0 or index>=self.lenth:
            return None
        elif index==0:
            return self.popfirst()
        elif index==self.lenth-1:
            return self.pop()
        pre= self.get_value(index-1)
        temp=pre.next
        pre.next=temp.next
        temp.next=None
        self.lenth-=1
        return temp
    def reverse(self):
        if self.head==None:
            print("list is empty")
            return
        temp=self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next #redundant
        before = None
        for _ in range(self.lenth):
            after = temp.next
            temp.next = before
            before = temp
            temp = after






my_linkedlist= LinkedList(4)
# print(my_linkedlist.head.value)
# my_linkedlist.printlist()
# my_linkedlist.append(5)
#
# my_linkedlist.pop()
# my_linkedlist.pop()
# my_linkedlist.pop()
# my_linkedlist.printlist()

# my_linkedlist.prepend(1)
# my_linkedlist.printlist()
# my_linkedlist.prepend(2)
# my_linkedlist.printlist()
#
# my_linkedlist.popfirst()
# my_linkedlist.printlist()
# my_linkedlist.popfirst()
# my_linkedlist.printlist()
# my_linkedlist.popfirst()
# my_linkedlist.printlist()

# my_linkedlist= LinkedList(0)
# # my_linkedlist.pop()
# my_linkedlist.append(1)
# my_linkedlist.append(2)
# my_linkedlist.append(3)
# my_linkedlist.reverse()
# my_linkedlist.printlist()