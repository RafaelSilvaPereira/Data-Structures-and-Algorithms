from abc import ABC

from LinearyStructures.NodeBasedStructures.DoubleReferNode import DoubleReferNode
from LinearyStructures.NodeBasedStructures.LinkedList import LinkedList

class DoubleLinkedList(LinkedList, ABC):

    def __init__(self):
        self.head = DoubleReferNode()
        object

    def isEmpty(self):
        return self.head.isNil()


    def size(self):
        current = self.head
        size = 0

        while not current.next.isNil():
            size += 1
            current = current.next
        return size

    def search(self, value):
        current = self.head
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
        current.setNext(DoubleReferNode())
        current.previous.setNext(current)
        if(isinstance(current.next, DoubleReferNode)):
            DoubleReferNode(current.next).setPrevious(current)
        else: raise Exception



a = DoubleLinkedList()

a.insert(10)