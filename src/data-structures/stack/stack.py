import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from node.node import Node

class Stack:
  def __init__(self, name):
    self.size = 0
    self.top_item = None
    self.limit = 1000
    self.name = name


  def push(self, value):
    """
    Adds data to the “top” of the stack
    """
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
    else:
      print("No more room!")


  def pop(self):
    """
    Provides and removes data from the top of the stack
    """
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    print("This stack is totally empty.")


  def peek(self):
    """
    Peek data from the top of the stack without removing it
    Throws an exception if the stack is empty
    """
    if not self.is_empty():
      return self.top_item.get_value()
    print("Nothing to see here!")


  def has_space(self):
    return self.limit > self.size


  def is_empty(self):
    """
    Check if the stack is empty
    """
    return self.size == 0


  def get_size(self):
    return self.size


  def get_name(self):
    return self.name


  def print_items(self):
    pointer = self.top_item
    print_list = []
    while (pointer):
      print_list.append(pointer.get_value())
      pointer = pointer.get_next_node()
    print_list.reverse()
    print("{0} Stack: {1}".format(self.get_name(), print_list))


  def are_brackets_matching(string):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"
    brackets_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for charatcer in string:
        if charatcer in opening_brackets:
            stack.append(charatcer)
        elif charatcer in closing_brackets:
            if not stack:
                return False
            top = stack.pop()
            if brackets_map[charatcer] != top:
                return False
        print(stack)

    return len(stack) == 0
