class Node:
    """
    Represents an individual node in the linked list.
    """

    def __init__(self, data=None):
        """
        Initializes a new instance of the Node class.
        """
        self.data = data
        self.next = None


class SinglyLinkedList:
    """
    Represents a singly linked list.
    """

    def __init__(self):
        """
        Initializes a new instance of the SinglyLinkedList class.
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

    def delete(self, data):
        """
        Deletes a node with the given data from the linked list.
        """
        if self.is_empty():
            print("Linked list is empty")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            print("Data not found in the linked list")
            return

        prev.next = current.next

    def display(self):
        """
        Displays the elements of the linked list.
        """
        if self.is_empty():
            print("Linked list is empty")
            return

        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Testing the implemented functionality
linked_list = SinglyLinkedList()
linked_list.display()  # Linked list is empty

linked_list.insert_at_beginning(10)
linked_list.insert_at_beginning(20)
linked_list.insert_at_end(30)
linked_list.insert_at_end(40)
linked_list.display()  # 20 10 30 40

linked_list.delete(30)
linked_list.display()  # 20 10 40

linked_list.delete(50)  # Data not found in the linked list
