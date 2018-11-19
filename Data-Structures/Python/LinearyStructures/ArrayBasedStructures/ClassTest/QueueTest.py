import unittest
from LinearyStructures.ArrayBasedStructures.Queue import Queue

class QueueTest(unittest.TestCase):


    def setUp(self):
        self._queue = Queue()
        self._otherQueue = Queue()

        for i in range(9):
            self._queue.add(i)

    def testIsEmpty(self):
        self.assertTrue( self._otherQueue.isEmpty )

    def testPeek(self):
        self.assertEqual(0,self._queue.peek())
        self.assertIsNone(self._otherQueue.peek())

    def testPoll(self):
        self.assertEqual(0, self._queue.poll())
        self.assertEqual(1, self._queue.peek())

    def testAddInQueue(self):
        self._otherQueue.add(33)
        self.assertEqual(33, self._otherQueue.peek())


