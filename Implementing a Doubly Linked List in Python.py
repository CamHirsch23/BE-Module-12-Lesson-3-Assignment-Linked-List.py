class Node:
    """
    Represents an individual node in the doubly linked list.
    """

    def __init__(self, data=None):
        """
        Initializes a new instance of the Node class.
        """
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """
    Represents a doubly linked list.
    """

    def __init__(self):
        """
        Initializes a new instance of the DoublyLinkedList class.
        """
        self.head = None

    def is_empty(self):
        """
        Checks if the linked list is empty.
        """
        return self.head is None

    def insert_at_beginning(self, data):
        """
        Inserts a new node at the beginning of the linked list.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        """
        Inserts a new node at the end of the linked list.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete(self, data):
        """
        Deletes a node with the given data from the linked list.
        """
        if self.is_empty():
            print("Linked list is empty")
            return

        if self.head.data == data:
            if self.head.next:
                self.head.next.prev = None
            self.head = self.head.next
            return

        current = self.head
        while current and current.data != data:
            current = current.next

        if current is None:
            print("Data not found in the linked list")
            return

        if current.next:
            current.next.prev = current.prev
        current.prev.next = current.next

    def display_forward(self):
        """
        Displays the elements of the linked list in forward order.
        """
        if self.is_empty():
            print("Linked list is empty")
            return

        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def display_backward(self):
        """
        Displays the elements of the linked list in backward order.
        """
        if self.is_empty():
            print("Linked list is empty")
            return

        current = self.head
        while current.next:
            current = current.next

        while current:
            print(current.data, end=" ")
            current = current.prev
        print()


# Testing the implemented functionality
linked_list = DoublyLinkedList()
linked_list.display_forward()  # Linked list is empty

linked_list.insert_at_beginning(10)
linked_list.insert_at_beginning(20)
linked_list.insert_at_end(30)
linked_list.insert_at_end(40)
linked_list.display_forward()  # 20 10 30 40
linked_list.display_backward()  # 40 30 10 20

linked_list.delete(30)
linked_list.display_forward()  # 20 10 40

linked_list.delete(50)  # Data not found in the linked list
