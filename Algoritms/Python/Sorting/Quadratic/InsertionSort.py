from Sorting.Util import swapInArray

def ordenedInsertion(array, start, end, index):
    for i in range(end, start - 1, -1):
        if array[index] < array[i]:

            swapInArray(array, index, i)
            index = i


def insertionSort(array):
    for i in range(0,len(array) - 1):
        ordenedInsertion(array, 0, i, i + 1)

