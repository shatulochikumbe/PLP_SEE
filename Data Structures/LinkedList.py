# Singly Linked List

# arr = [[]->10, {]20, []30, []40, []50]
#
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    # Add to front    
    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

     #Print list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_front(30)
    ll.insert_front(20)
    ll.insert_front(10)
    ll.print_list()

# LIFO

# Doubly Linked List

class DNone:
    def __init__(self, data):
        self.data = data
        self.Prev = None
        self.Next = None
