package Util;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Util {

	public static void Swap(Object[] collection, int indexA, int indexB) {
		Object obj = collection[indexA];
		collection[indexA] = collection[indexB];
		collection[indexB] = obj;
	}

	public static Integer[] RandomList(int range) {

		ArrayList<Integer> array = new ArrayList<>();
		Random randInt = new Random();

		/*
		 * this case is so that the smallest number generated randomly, not in module,
		 * is greater than the largest number of the array (it generates problems with
		 * couting sort)
		 */
		array.add(Integer.MAX_VALUE / 100);

		for (int i = 0; i < range - 1; i++) {

			int randomValue = randInt.nextInt(range);
			
			array.add(randomValue);

		}

		return array.toArray(new Integer[range]);
	}

	public static int max(Integer[] array) {
		int ans = Integer.MIN_VALUE;
		for (int i = 0; i < array.length; i++) {
			if (array[i] > ans) {
				ans = array[i];
			}
		}
		return ans;

	}

	public static int min(Integer[] tempArray) {
		int ans = Integer.MAX_VALUE;
		for (int i = 0; i < tempArray.length; i++) {
			if (tempArray[i] < ans) {
				ans = tempArray[i];
			}
		}
		return ans;

	}

}
