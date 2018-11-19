class ArraysIndexOfBounds(IndexError):
    def __init__(self, expectedIndex, arraySize):
        self.expectedIndex = expectedIndex
        self.arraySize = arraySize

    def __str__(self):
        return IndexError.__str__() + " exception raised because the expected index is {x}, but the list size is {y}".format(x=self.expectedIndex,y=self.arraySize)

class IncompatibleSizesException(ArraysIndexOfBounds):

    def __init__(self, sizeOfOriginArray=None, sizeOfDestinyArray=None):
        self.sizeA = sizeOfOriginArray
        self.sizeB = sizeOfDestinyArray

    def __str__(self):
        return "oparation not is compatible, the size of origin array {one} less than the size of destiny array {two}".format(one=self.sizeA,two=self.sizeB)


class ElementNotContained(Exception):

    def __init__(self,element,arr):
        self.element = element
        self.arr = arr

    def __str__(self,element,arr):
        return "and element {x} does not belong to list {y}".format(x=self.element,y=self.arr)

class ArrayList:
    """
        For educational purposes only, this class is a simplified implementation of the Java Array List class.
    """
    def __init__(self, initalSize=10):
        self._array = [None] * initalSize
        self._currentIndex =  0
        self._capacity = initalSize


    def isEmpty(self):
        return self._currentIndex == 0


    def getElement(self, index):
        newIndex = index

        if index < 0:
            newIndex = self._currentIndex + index
        if newIndex > self._currentIndex:
            raise ArraysIndexOfBounds
        return self._array[index]

    def add(self, element):
        if self._checkCapacity():
            self._array[self._currentIndex] = element
            self._currentIndex += 1
        else:
            self._increseCapacity()
            self.add(element)


    def remove(self, index=None):
        """
        removes an element specified by Index
        
        :param index: None by default, in this case, the remove will work like a pop. 
        :return: element in that index.
        """

        if index is None:
            index = self._currentIndex
        ans = self.getElement(index)

        self._rightShift(index, self._currentIndex)
        self._currentIndex -= 1
        return  ans

    def removeElement(self, element):
        """
        remove a element in arraylist from its value.
        :param element: element to be removed
        """
        index = None
        for i in range(len(self._array)):
            if self._array[i] == element:
                index = i
                break
        if index is None:
            raise ElementNotContained(element, self._array)
        self.remove(index)

    def copyTo(self, origin :list, destiny: list):
        sizeOrigin = len(origin)
        sizeDestiny = len(destiny)
        if sizeDestiny < sizeOrigin:
            raise IncompatibleSizesException(sizeOrigin, sizeDestiny)
        for i in range(sizeOrigin):
            destiny[i] = origin[i]

    def copy(self, array, start=None, stop=None):
        size = len (array)
        if start is None: start = 0
        if stop is None: stop = size

        newArray = [None] * size
        for i in range(start, stop): newArray[i] = array[i]
        return array

    def _rightShift(self, startIndex, lastIndex):
        for i in range(startIndex, lastIndex):
            self._array[i] = self._array[i + 1]

    def _checkCapacity(self):
        return self._capacity * 0.75 <= self._currentIndex

    def _increseCapacity(self):
        newCapacity = self._capacity * 1.75
        newArray = [None] * newCapacity

        self.copyTo(self._array, newArray)
        self._array = newArray


        



