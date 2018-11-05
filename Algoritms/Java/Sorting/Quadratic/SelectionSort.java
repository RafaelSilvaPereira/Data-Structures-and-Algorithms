package Quadratic;

import Util.Util;

public class SelectionSort<T extends Comparable<T>> {

	private int SelectSmaller(T[] array, int startIndex, int endIndex) {
		int SmallerIndex = startIndex;

		for (int i = startIndex; i < endIndex; i++) {
			if (array[i].compareTo(array[SmallerIndex]) < 0) {
				SmallerIndex = i;
			}
		}
		return SmallerIndex;
	}

	public void Sort(T[] array) {
		int arrayLength = array.length;
		for (int i = 0; i < arrayLength; i++) {
			int indexSmaller = SelectSmaller(array, i, arrayLength);
			Util.Swap(array, i, indexSmaller);
		}
	}
}
