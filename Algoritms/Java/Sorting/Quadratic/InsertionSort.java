package Quadratic;

import Util.Util;

public class InsertionSort<T extends Comparable<T>> {
	private void OrderlyInsertion(T[] array, int start, int end, int currentIndex) {
		for (int i = end; i >= start; i--) {
			if (array[currentIndex].compareTo(array[i]) < 0) {
				Util.Swap(array, currentIndex, i);
				currentIndex = i;
			}
		}
	}

	public void Sort(T[] array) {
		for (int i = 0; i < array.length - 1; i++) {
			OrderlyInsertion(array, 0, i, i + 1);
		}
	}
}
