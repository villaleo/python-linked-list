# -----------------------------------------
# Author: Leonardo Villalobos
# Date: 4/21ß/2021
# Description: Construct a linked list data
# structure class with various methods.
# -----------------------------------------
import Node as nd


class LinkedList:
    """
    Construct a linked list data structure.

    + Add items using `addFirst(item: int)` or `addLast(item: int)`.

    + Delete items using `deleteFirst()` or `deleteLast()`.

    + Check if an item is in the linked list using `contains(item: int)`.

    + Grab the index of the first occurance of an item using `indexOf(item: int)`.

    + Grab the size of the linked list using `size()`.

    + Make a list representation of the linked list using `toList()`.

    + Reverse the linked list in place using `reverse()`.
    """
    first: nd.Node
    last: nd.Node
    count: int

    def __init__(self):
        """
        Construct an empty linked list.
        """
        self.first = None
        self.last = None
        self.count = 0

    def __isEmpty(self) -> bool:
        """
        Returns `True` if the linked list is empty.
        """
        return self.first == None

    def __getPrevious(self, node: nd.Node) -> nd.Node:
        """
        Returns the previous node of a node object.

        + `node: nd.node` -- A node object.
        """
        if self.__isEmpty():
            raise TypeError("Cannot get previous item from empty linked list.")
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
        Add `item` to the beginning of the linked list.

        + `item: int` -- the item which will be added.
        """
        node = nd.Node(item)

        if self.__isEmpty():
            self.first = self.last = node
        else:
            node.nextNode = self.first
            self.first = node

        self.count += 1

    def addLast(self, item: int) -> None:
        """
        Add `item` to the end of the linked list.

        + `item: int` -- the item which will be added.
        """
        node = nd.Node(item)

        if (self.__isEmpty()):
            self.first = self.last = node
        else:
            self.last.nextNode = node
            self.last = node

        self.count += 1

    def deleteFirst(self) -> None:
        """
        Delete the first item in the linked list.
        """
        if self.__isEmpty():
            raise TypeError("Cannot remove item from empty linked list")
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
        Delete the last item in the linked list.
        """
        if self.__isEmpty():
            raise TypeError("Cannot remove item from empty linked list")
        if self.first == self.last:
            self.first = self.last = None
        else:
            previous = self.__getPrevious(self.last)
            self.last = previous
            self.last.nextNode = None

        self.count -= 1

    def contains(self, item: int) -> bool:
        """
        Returns `True` if `item: int` is found within
        the linked list. `False` otherwise.

        + `item: int` -- the item being search for within the linked list.
        """
        return self.indexOf(item) != -1

    def indexOf(self, item: int) -> int:
        """
        Returns the index of the first occurence of `item`.

        + `item: int` -- the item in question.
        """
        index = 0
        current = self.first

        while current != None:
            if current.value == item:
                return index
            current = current.nextNode
            index += 1
        return -1

    def size(self) -> int:
        """
        Returns the size of the linked list.
        """
        return self.count

    def toList(self) -> list:
        """
        Returns a list representation of the linked list
        """
        temp = list()
        index = 0
        current = self.first

        while current != None:
            temp.append(current)
            current = current.nextNode
        return temp

    def reverse(self) -> None:
        """
        Reverses the linked list.
        """
        if self.__isEmpty():
            return None
        previous = self.first
        current = self.first.nextNode
        while current != None:
            n = current.nextNode
            current.nextNode = previous
            previous = current
            current = n

        self.last = self.first
        self.last.nextNode = None
        self.first = previous
