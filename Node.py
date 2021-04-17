# -----------------------------------------
# Author: Leonardo Villalobos
# Date: 4/17/2021
# Description: A simple Node class. Each
# node contains a value and a reference
# to the next node.
# -----------------------------------------

class Node:
    value = 0
    nextNode = None

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)
