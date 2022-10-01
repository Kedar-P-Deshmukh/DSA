class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTreee:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if temp.value == new_node.value:
                return False
            elif new_node.value<temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left

            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self,value):
        temp = self.root
        while temp is not None:
            if value<temp.value:
                temp = temp.left
            elif value>temp.value:
                temp = temp.right
            else:
                return True
        return False

    def min_value_node(self,current_node:Node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

        # ------------------------BFS-------------------------------------

    def BFS(self):
        currunt_node = self.root
        queue = []
        results = []
        queue.append(currunt_node)

        while len(queue)>0:
            currunt_node = queue.pop(0)
            results.append(currunt_node.value)
            if currunt_node.left is not None:
                queue.append(currunt_node.left)
            if currunt_node.right is not None:
                queue.append(currunt_node.right)
        return results

    #---------------------------DFS-----------------------------------

    def DFS_pre_order(self):
        result = []
        def traverse(current_node):
            result.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return result

    def DFS_post_order(self):
        result = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            result.append(current_node.value)

        traverse(self.root)
        return result

    def DFS_in_order(self):
        result = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            result.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)


        traverse(self.root)
        return result




my_bst = BinarySearchTreee()

# my_bst.insert(2)
# my_bst.insert(1)
# my_bst.insert(3)
# print(my_bst.root.value)
# print(my_bst.root.left.value)
# print(my_bst.root.right.value)

for i in [47,21,76,18,27,52,82]:
    my_bst.insert(i)


# print(my_bst.contains(21))
# print(my_bst.contains(17))
#
#
# # print(my_bst.root.value)
# # print(my_bst.root.left.value)
# # print(my_bst.root.right.value)
#
print(my_bst.min_value_node(my_bst.root).value)
print(my_bst.min_value_node(my_bst.root.right).value)

print(my_bst.BFS()) #bfs
print(my_bst.DFS_pre_order())
print(my_bst.DFS_post_order())
print(my_bst.DFS_in_order())