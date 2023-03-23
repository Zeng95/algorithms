# A Node is a data structure that stores a value that can be of any data type and has a pointer to another node.
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    # Insert a new head node
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.get_head_node())
        self.head_node = new_node

    # Insert a new tail node
    def insert_end(self, new_value):
        new_node = Node(new_value)
        current_node = self.head_node

        while current_node.get_next_node() is not None:
            current_node = current_node.get_next_node()
        current_node.set_next_node(new_node)

    # Return all the nodes in the list as a string
    def stringify_list(self):
        string_list = "["
        current_node = self.head_node

        while current_node is not None:
            # Use str() to convert integers to strings
            string_list += str(current_node.value)
            if current_node.get_next_node() is not None:
                string_list += ", "
            current_node = current_node.get_next_node()

        string_list += "]"
        return string_list

    # Remove the first node that contains a particular value
    def remove_node(self, value_to_remove):
        current_node = self.head_node

        # If the head node is the one to be deleted
        if current_node.value == value_to_remove:
            current_node = current_node.get_next_node()
            return

        # Traverse the linked list to find the node to be deleted
        prev_node = None
        while current_node.value != value_to_remove:
            prev_node = current_node
            current_node = prev_node.get_next_node()

        # If the node to be deleted is not found
        if current_node is None:
            return

        # Remove the node by connecting the previous node to the next node
        prev_node.next_node = current_node.get_next_node()
        current_node = None

ll = LinkedList(10)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
ll.insert_end(100)
ll.insert_end(103)
ll.insert_end(102)
ll.insert_end(103)
print(ll.stringify_list())

ll.remove_node(103)
print(ll.stringify_list())
