package TestClass;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import LinearyTime.CountingSort;
import NLogN.MergeSort;
import NLogN.QuickSort;
import Quadratic.BubbleSort;
import Quadratic.InsertionSort;
import Quadratic.SelectionSort;
import Util.Util;

public class AllSortingTest {

	private BubbleSort<Integer> bbs = new BubbleSort<>();
	private InsertionSort<Integer> ins = new InsertionSort<>();
	private SelectionSort<Integer> sns = new SelectionSort<>();
	private QuickSort<Integer> qks = new QuickSort<>();
	private MergeSort<Integer> mgs = new MergeSort<>();
	private CountingSort cgs = new CountingSort();
	private Integer[] array = Util.RandomList(30);

	private boolean isOrdened(Integer[] array) {
		boolean ans = true;

		for (int i = 1; i < array.length; i++) {
			if (array[i] < array[i - 1]) {
				ans = false;
				break;
			}
		}
		return ans;
	}

	@Test
	public void BubbleSortTest() {
		assertFalse(this.isOrdened(array));
		bbs.Sort(array);
		assertTrue(this.isOrdened(array));

	}

	@Test
	public void SelectionSortTest() {
		assertFalse(this.isOrdened(array));
		sns.Sort(array);
		assertTrue(this.isOrdened(array));

	}

	@Test
	public void InsertionSortTest() {
		assertFalse(this.isOrdened(array));
		ins.Sort(array);
		assertTrue(this.isOrdened(array));

	}

	@Test
	public void MergeSortTest() {
		assertFalse(this.isOrdened(array));
		mgs.Sort(array);
		assertTrue(this.isOrdened(array));

	}

	@Test
	public void QuickSortTest() {
		assertFalse(this.isOrdened(array));
		qks.Sort(array);
		assertTrue(this.isOrdened(array));

	}

	@Test
	public void CountingSortTest() {
		assertFalse(this.isOrdened(array));
		cgs.Sort(array);
		assertTrue(this.isOrdened(array));

	}

}
