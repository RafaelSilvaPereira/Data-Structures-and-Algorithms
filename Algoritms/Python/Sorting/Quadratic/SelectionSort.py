from Sorting.Util import swapInArray


def selectMin(array, i, j):
    smallerIndex = i

    for k in range(i,j):
        if array[k] < array[smallerIndex]:
            smallerIndex = k
    return smallerIndex


def SelectionSort(array):
    for i in range(len(array)):
        min = selectMin(array, i, len(array))
        swapInArray(array,i,min)