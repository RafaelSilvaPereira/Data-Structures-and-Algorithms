from LinearyStructures.NodeBasedStructures.Node import Node
import abc
class LinkedList:

    @abc.abstractclassmethod
    def __init__(self):
        pass

    @abc.abstractclassmethod
    def isEmpty(self):
        pass
    @abc.abstractclassmethod
    def size(self):
        pass

    @abc.abstractclassmethod
    def search(self, value):
        pass

    @abc.abstractclassmethod
    def insert(self, value):
        pass

    @abc.abstractclassmethod
    def remove(self, value):
        pass

