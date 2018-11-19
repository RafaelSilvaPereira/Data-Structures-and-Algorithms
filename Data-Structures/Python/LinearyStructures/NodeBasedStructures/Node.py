class Node:

    def __init__(self,data=None, next=None):
        self.data = data
        if not(data is None):
            if next is None: next = Node()

        self.next = next

    def isNil(self):
        return self.data is None;

    def __str__(self):
        ans = ""
        if not self.isNil():
            strNextValue = self.next.data
            if strNextValue is None:
                strNextValue = "NIL"

            ans += "Node Value: {value}, your next is {nextValue}".format(value=self.data, nextValue= strNextValue)
        else:
            ans += "NIL"
        return ans

    def __eq__(self, other):
        return self.data == other.value and self.next == other.next

    def setValue(self, value):
        self.data = value

    def setNext(self, next):
        if isinstance(next, Node):
            self.next = next
        else:
            raise TypeError


