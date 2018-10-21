from Sorting import Util

class QuickSort:

    def partition(self, array, start, end):  # Lomuto Partition
        pivot = start

        for i in range(start, end):
            if array[i] <= array[end]:
                Util.swapInArray(array, pivot, i)
                pivot += 1
        Util.swapInArray(array, pivot, end)
        return pivot

    def sort(self, array, start, end):
        if start < end:
            pivot = self.partition(array, start, end)
            self.Quick(array, start, pivot - 1)
            self.Quick(array, pivot + 1, end)

    def sort(self, array):
        self.sort(array, 0, len(array) - 1)