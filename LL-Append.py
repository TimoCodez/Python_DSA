# Define the Node class for the linked list
class Node:
    # Constructor for the Node class
    def __init__(self, value):
        self.value = value  # Set the value of the node to the passed value
        self.next = None  # Initialize the next pointer of the node to None


# Define the LinkedList class
class LinkedList:
    # Constructor for the LinkedList class
    def __init__(self, value):
        new_node = Node(value)  # Create a new node with the passed value
        self.head = new_node  # Set the head of the linked list to the new node
        self.tail = new_node  # Set the tail of the linked list to the new node
        self.length = 1  # Set the initial length of the linked list to 1

    # Method to print all the values in the linked list
    def print_list(self):
        temp = self.head  # Start from the head of the linked list
        while temp is not None:  # Traverse until the end of the list
            print(temp.value)  # Print the value of the current node
            temp = temp.next  # Move to the next node

    # Method to make the linked list empty
    def make_empty(self):
        self.head = None  # Set the head to None
        self.tail = None  # Set the tail to None
        self.length = 0  # Reset the length to 0

    # Method to append a new value to the end of the linked list
    def append(self, value):
        new_node = Node(value)  # Create a new node with the passed value
        if self.head is None:  # Check if the linked list is empty
            self.head = new_node  # Set the head to the new node
            self.tail = new_node  # Set the tail to the new node
        else:
            self.tail.next = new_node  # Connect the current tail's next to the new node
            self.tail = new_node  # Update the tail to the new node
        self.length += 1  # Increase the length of the linked list by 1


# Create a new linked list with an initial value of 1
my_linked_list = LinkedList(1)
my_linked_list.make_empty()  # Empty the linked list

# Add values 1 and 2 to the list
my_linked_list.append(1)
my_linked_list.append(2)

# Print the head, tail, and length of the linked list
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')

# Print all the values in the linked list
print('Linked List:')
my_linked_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    Head: 1
    Tail: 2
    Length: 2 

    Linked List:
    1
    2

"""
