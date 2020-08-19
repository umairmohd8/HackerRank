class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        new_node = Node(data)
        if head is None:
            self.head = new_node
            return new_node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        return new_node


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)