from abc import ABC
from LinearyStructures.NodeBasedStructures.Node import Node
from LinearyStructures.NodeBasedStructures.LinkedList import LinkedList

class SingleLinkedList(LinkedList):

    def __init__(self):
        self.head = Node()

    def isEmpty(self):
        return  self.head.isNil()

    def size(self):
        current = self.head
        size = 0

        while not current.next.isNil():
            size += 1
            current = current.next
        return size
    def search(self, value):
        ans = None
        current = self.head
        while current.data != value and not current.isNil():
            current = current.next

        if not current.isNil():
            ans = current
        return ans

    def insert(self, value):

        current = self.head
        while not current.isNil():
            current = current.next
        current.setValue(value)
        current.setNext(Node())

    def remove(self, value):
        ans = None
        current = self.head
        if self.head.data == value:
            ans = self.head
            self.head = self.head.next
        else:
            previous = Node()
            while not current.isNil() and current.data != value:
                previous = current
                current = current.next

            if not current.isNil():
                previous.setNext(current.next)
                ans = current
            else: return None

        return ans

a = SingleLinkedList()
a.insert(20)
a
