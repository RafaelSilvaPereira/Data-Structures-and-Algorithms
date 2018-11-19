from LinearyStructures.NodeBasedStructures.Node import Node
class DoubleReferNode(Node):

    def __init__(self, data=None, previous=None, next=None):
        super(DoubleReferNode, self).__init__(data, next)
        if not data is None:
            if(previous is None): previous = DoubleReferNode()
            self.previous: DoubleReferNode = previous
        else:
            self.previous = previous

    def __str__(self):
        ans = ""
        strNextValue = self.next.data
        if strNextValue is None:
            strNextValue = "NIL"
        strPrevValue = self.previous.data
        if strPrevValue is None:
            strPrevValue = "NIl"


        if not self.isNil ():
            ans += "Node Value: {value}, your previous is {prev} and your next is {nextValue}".format(value=self.data,prev=strPrevValue, nextValue= strNextValue)
        else:
            ans += "NIL"
        return ans
    def __eq__(self, other):
        return isinstance(other, DoubleReferNode) and self.data == other.value and self.next == other.next and self.previous == other.previous


    def setPrevious(self, previous):
        if isinstance(previous, Node):
            self.next = previous
        else:
            raise TypeError

    def getPrevious(self):
        return self.previous