import unittest
from Sorting.Quadratic.BubbleSort import BubbleSort
from Sorting.Quadratic.InsertionSort import InsertionSort
from Sorting.Quadratic.SelectionSort import SelectionSort
from Sorting.NLogN.QuickSort import QuickSort
from  Sorting.NLogN.MergeSort import MergeSort
from Sorting.LinearyTime.CountingSort import CountingSort
from Sorting import Util

class AllSortingTest(unittest.TestCase):


    def setUp(self):
        self.bbs = BubbleSort ()
        self.ins = InsertionSort ()
        self.sns = SelectionSort ()
        self.qks = QuickSort ()
        self.mgs = MergeSort ()
        self.cgs = CountingSort ()
        self.array = Util.randomList(7000)

    def testBubbleSort(self):
        self.bbs.sort(self.array)
        self.assertTrue(Util.isOrdened(self.array))

    def testSelectionSort(self):
        self.sns.sort(self.array)
        self.assertTrue (Util.isOrdened(self.array))

    def testInsertionSort(self):
        self.ins.sort(self.array)
        self.assertTrue (Util.isOrdened(self.array))

    def testMergeSort(self):
        self.mgs.sort(self.array)
        self.assertTrue (Util.isOrdened(self.array))

    def testQuickSort(self):
        self.qks.sort(self.array)
        self.assertTrue (Util.isOrdened(self.array))

    def testCountingSort(self):
        self.cgs.sort(self.array)
        self.assertTrue (Util.isOrdened(self.array))