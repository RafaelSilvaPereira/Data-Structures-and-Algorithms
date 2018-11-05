package NLogN;

import java.util.Arrays;

public class MergeSort<T extends Comparable<T>> {

	private void Merge(T[] array, int start, int middle, int end) {
		int arrayLength = array.length;
		T[] copy = Arrays.copyOf(array, arrayLength);

		int indexA = start;
		int indexB = middle + 1;

		int indexK = start;

		while (indexA <= middle && indexB <= end) {
			if (copy[indexA].compareTo(copy[indexB]) < 0) {
				array[indexK++] = copy[indexA++];
			} else {
				array[indexK++] = copy[indexB++];
			}

		}

		while (indexA <= middle) {
			array[indexK++] = copy[indexA++];
		}

		while (indexB <= end) {
			array[indexK++] = copy[indexB++];
		}
	}

	public void Sort(T[] array) {
		this.Sort(array, 0, array.length - 1);
	}

	private void Sort(T[] array, int start, int end) {
		if (start < end) {
			int middle = (start + end) / 2;

			this.Sort(array, start, middle);
			this.Sort(array, middle + 1, end);

			this.Merge(array, start, middle, end);

		}
	}
}
