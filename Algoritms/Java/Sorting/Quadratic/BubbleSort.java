package Quadratic;

import Util.Util;

public class BubbleSort<T extends Comparable> {

	public void Sort(T[] array) {
		for (int i = 0; i < array.length; i++) {
			for (int j = 0; j < array.length - 1; j++) {

				if (array[j].compareTo(array[j + 1]) >= 1) {
					Util.Swap(array, j, j + 1);
				}
			}
		}
	}
}
