from Sorting.Util import swapInArray

class SelectionSort:
    def selectMin(self,array, i, j):
        smallerIndex = i

        for k in range(i,j):
            if array[k] < array[smallerIndex]:
                smallerIndex = k
        return smallerIndex


    def sort(self,array):
        for i in range(len(array)):
            min = self.selectMin(array, i, len(array))
            swapInArray(array,i,min)