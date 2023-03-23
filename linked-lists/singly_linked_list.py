# A Node is a data structure that stores a value that can be of any data type and has a pointer to another node.
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next

    def set_next_node(self, next):
        self.next = next


class LinkedList:
    def __init__(self, value=None):
        self.head = Node(value)

    def get_head_node(self):
        return self.head

    # Insert a new head node
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.get_head_node())
        self.head = new_node

    # Insert a new tail node
    def insert_end(self, new_value):
        new_node = Node(new_value)
        current = self.head

        while current.get_next_node() is not None:
            current = current.get_next_node()
        current.set_next_node(new_node)

    # Return all the nodes in the list as a string
    def stringify_list(self):
        string_list = "["
        current = self.head

        while current is not None:
            # Use str() to convert integers to strings
            string_list += str(current.value)
            if current.get_next_node() is not None:
                string_list += ", "
            current = current.get_next_node()

        string_list += "]"
        return string_list

    # Remove the first node that contains a particular value
    def remove_node(self, value_to_remove):
        current = self.head

        # If the head node is the one to be deleted
        if current.value == value_to_remove:
            current = current.get_next_node()
            return

        # Traverse the linked list to find the node to be deleted
        prev = None
        while current.value != value_to_remove:
            prev = current
            current = prev.get_next_node()

        # If the node to be deleted is not found
        if current is None:
            return

        # Remove the node by connecting the previous node to the next node
        prev.next = current.get_next_node()
        current = None

    def remove_nodes(self, value_to_remove):
        # Handle case where head node has the value to remove
        while self.head is not None and self.head.value == value_to_remove:
            self.head = self.head.get_next_node()

        # Traverse the linked list using two pointers
        prev = None
        current = self.head
        while current is not None:
            if current.value == value_to_remove:
                # Remove current node by updating previous node's next pointer
                prev.next = current.next
            else:
                # Update previous pointer to current node
                prev = current
            # Move current pointer to next node
            current = current.next


ll = LinkedList(10)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
ll.insert_end(100)
ll.insert_end(103)
ll.insert_end(102)
ll.insert_end(103)
ll.insert_end(70)
print(ll.stringify_list())
ll.remove_nodes(70)
print(ll.stringify_list())
