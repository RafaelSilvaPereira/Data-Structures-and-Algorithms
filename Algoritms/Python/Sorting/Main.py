from Sorting.Quadratic.BubbleSort import BubbleSort
from Sorting.Quadratic.InsertionSort import InsertionSort
from Sorting.Quadratic.SelectionSort import SelectionSort


bb = BubbleSort()
ins = InsertionSort()
slc = SelectionSort()

array = [5, 3, 2, 1]
slc.sort(array)
print(array)