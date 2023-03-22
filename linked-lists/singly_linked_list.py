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
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    # Insert a new tail node
    def insert_end(self, new_value):
        new_node = Node(new_value)
        current_node = self.head_node

        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = new_node

    # Return all the nodes in the list as a string
    def stringify_list(self):
        string_list = "["
        current_node = self.head_node

        while current_node is not None:
            # Use str() to convert integers to strings
            string_list += str(current_node.value)
            if current_node.next_node is not None:
                string_list += ", "
            current_node = current_node.next_node

        string_list += "]"
        return string_list


ll = LinkedList(True)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
ll.insert_end(100)
ll.insert_end(101)
ll.insert_end(102)
ll.insert_end(103)
print(ll.stringify_list())
