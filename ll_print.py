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

    # Method to append a new value to the end of the linked list
    def append(self, value):
        new_node = Node(value)  # Create a new node with the passed value
        if self.length == 0:  # Check if the linked list is empty
            self.head = new_node  # Set the head to the new node
            self.tail = new_node  # Set the tail to the new node
        else:
            self.tail.next = new_node  # Connect the current tail's next to the new node
            self.tail = new_node  # Update the tail to the new node
        self.length += 1  # Increase the length of the linked list by 1
        return True  # Return True indicating successful addition


# Create a new linked list with an initial value of 11
my_linked_list = LinkedList(11)
my_linked_list.append(3)  # Append value 3 to the list
my_linked_list.append(23)  # Append value 23 to the list
my_linked_list.append(7)  # Append value 7 to the list

# Print all the values in the linked list
my_linked_list.print_list()
