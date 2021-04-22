# -----------------------------------------
# Author: Leonardo Villalobos
# Date: 4/21/2021
# Description: A simple Node class. Each
# node contains a value and a reference
# to the next node.
# -----------------------------------------

class Node:
    """
    Construct a node object. Each node holds a `value: int` and
    a reference to the next node, `nextNode: Node`.
    """
    value = 0
    nextNode = None

    def __init__(self, value: int):
        """
        Construct a node object with `value` assigned for the value.
        """
        self.value = value

    def __repr__(self):
        """
        String representation of the node object.
        """
        return str(self.value)
