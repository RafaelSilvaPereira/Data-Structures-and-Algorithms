package LinearyTime;

import Util.Util;

public class CountingSort {

	public void Sort(Integer[] array) {
		int smaller = Util.min(array);
		int keyValue = 0;
		if (smaller < 0)
			keyValue = 1 - smaller;

		int lenArray = array.length;
		Integer[] tempArray = new Integer[lenArray];

		for (int i = 0; i < lenArray; i++)
			tempArray[i] = array[i] + keyValue;

		int bigger = Util.max(tempArray);
		smaller = Util.min(tempArray);
		int size = (bigger - smaller) + 2;

		int[] contArray = new int[size];

		for (int i = 0; i < tempArray.length; i++)
			contArray[tempArray[i] - smaller + 1]++;
		for (int i = 1; i < contArray.length; i++)
			contArray[i] += contArray[i - 1];

		for (int i = 0; i < lenArray; i++) {
			array[contArray[tempArray[i] - smaller + 1] - 1] = tempArray[i];
			contArray[tempArray[i] - smaller + 1]--;
		}
	}
}
