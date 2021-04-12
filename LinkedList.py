# -----------------------------------------
# Author: Leonardo Villalobos
# Date: 4/12/2021
# Description: Construct a Linked List data
# structure class with various methods.
# -----------------------------------------
import Node as nd


class LinkedList:
    first: nd.Node
    last: nd.Node
    count: int

    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0

    def isEmpty(self) -> bool:
        """
        Returns True if the Linked List is empty.
        """
        return self.first == None

    def getPrevious(self, node: nd.Node) -> nd.Node:
        """
        Returns the previous node of a node object.

        *node: nd.node -- A node object.
        """
        if self.isEmpty():
            raise TypeError(
                "There is no previous item, for the list is empty.")
        if self.first == self.last:
            self.first = self.last = None
        current = self.first
        while current != None:
            if current.nextNode == node:
                return current
            current = current.nextNode
        return None

    def addFirst(self, item: int) -> None:
        """
        Add item to the beggining of the Linked List.

        *item: int -- the item being added to the front of the Linked List.
        """
        node = nd.Node(item)
        # create a variable, node, which holds a new node
        # object with the item assigned to the value.
        if self.isEmpty():
            self.first = self.last = node
            # if the front of the LinkedList is empty, set the
            # first and last (front and back) of the LinkedList
            # to point to 'node'.
        else:
            node.nextNode = self.first
            self.first = node
            # otherwise, the current node's 'nextNode' variable
            # points to the this front (first) and this front
            # (first) points to the 'node'.
        self.count += 1

    def addLast(self, item: int) -> None:
        """
        Add item to the end of the Linked List.

        *item: int -- the item to add to the back of the Linked List.
        """
        node = nd.Node(item)
        if (self.isEmpty()):
            self.first = self.last = node
        else:
            self.last.nextNode = node
            self.last = node
        self.count += 1

    def deleteFirst(self) -> None:
        """
        Delete the first item in the Linked List.
        """
        if self.isEmpty():
            raise TypeError("Cannot remove item from empty list")
        if self.first == self.last:
            self.first = self.last == None
            return
        else:
            second = self.first.nextNode
            self.first.nextNode = None
            self.first = second
        self.count -= 1

    def deleteLast(self) -> None:
        """
        Delete the last item in the Linked List.
        """
        if self.isEmpty():
            raise TypeError("Cannot remove item from empty list")
        if self.first == self.last:
            self.first = self.last = None
        else:
            previous = self.getPrevious(self.last)
            self.last = previous
            self.last.nextNode = None
        self.count -= 1

    def contains(self, item: int) -> bool:
        """
        Returns True if the item is found within
        the LinkedList. False otherwise.

        *item: int -- the item being search for within the Linked List.
        """
        return self.indexOf(item) != -1

    def indexOf(self, item: int) -> int:
        """
        Returns the index of the first occurence of the item.

        *item: int -- the item within the Linked List.
        """
        index = 0
        current = self.first
        # current gets assigned to the first node
        while current != None:
            if current.value == item:
                # if the current node's value is equal
                # to the item we are looking for,
                # return True
                return index
            # update current node to the next node
            current = current.nextNode
            index += 1
        return -1

    def size(self) -> int:
        """
        Returns the size of the Linked List.
        """
        return self.count

    def toList(self) -> list:
        """
        Returns a list representation of the Linked List
        """
        temp = []
        index = 0
        current = self.first
        while current != None:
            temp.append(current.value)
            current = current.nextNode
        return temp
