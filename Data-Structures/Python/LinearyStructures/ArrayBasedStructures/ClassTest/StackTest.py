import unittest
from LinearyStructures.ArrayBasedStructures.Stack import Stack, StackUnderFlowException


class StackTest(unittest.TestCase):


    def setUp(self):
        self.stack = Stack()
        self.otherStack = Stack()
        for elements in range(0, 11):
            self.stack.push(elements)

    def testStackIsCreated(self):
        self.assertIsNotNone(self.stack)

    def testIsEmpty(self):
        self.assertTrue(self.otherStack.isEmpty())

    def testPopRaiseException(self):
        self.assertTrue(self.otherStack.isEmpty())
        try:
            self.otherStack.pop()
        except StackUnderFlowException:
            pass


    def testPushElements(self):
        for elements in range(0, 10):
            self.otherStack.push(elements)
            self.assertEqual(elements + 1, self.otherStack.elements())

    def testTop(self):
        self.assertEqual(self.stack.top(), 10)
        self.stack.push(23)
        self.assertEqual(self.stack.top(), 23)

    def testPop(self):
        self.assertEqual(11, self.stack.elements())
        self.assertEqual(self.stack.pop(), 10)
        self.assertEqual(self.stack.top(), 9)
        self.assertEqual(self.stack.elements(), 10)

