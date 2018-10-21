from Sorting.Util import swapInArray

class InsertionSort:

    def ordenedInsertion(self,array, start, end, index):
        for i in range(end, start - 1, -1):
            if array[index] < array[i]:

                swapInArray(array, index, i)
                index = i


    def sort(self,array):
        for i in range(0,len(array) - 1):
            self.ordenedInsertion(array, 0, i, i + 1)

