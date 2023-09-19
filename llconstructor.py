# Definition of the Node class to represent individual elements of the linked list.
class Node:
    # Constructor for the Node class
    def __init__(self, value):
        self.value = value  # Assign the provided value to the node's value attribute.
        self.next = None  # Initialize the next attribute to None. It will point to the next node in the list when set.


# Definition of the LinkedList class to represent the entire linked list.
class LinkedList:
    # Constructor for the LinkedList class
    def __init__(self, value):
        new_node = Node(value)  # Create a new node with the given value.
        self.head = new_node  # Set the head of the linked list to the newly created node.
        self.tail = new_node  # Similarly, set the tail of the linked list to the newly created node.
        self.length = 1  # Initialize the length of the linked list to 1 since we've added one node.

# Instantiate a new linked list with an initial value of 4.
my_linked_list = LinkedList(4)

# Print the value of the head of the linked list. It should print 4.
print(my_linked_list.head.value)