package NLogN;

import Util.Util;

public class QuickSort<T extends Comparable<T>> {

	
	private int LomutoPartition(T[] array, int start, int end)
    {
        int pivot = start;

        for (int i = start; i < end; i++)
        {
            if (array[i].compareTo(array[end]) < 0)
            {
                Util.Swap(array, pivot++, i);

            }
        }

        Util.Swap(array, pivot, end);
        return pivot;
    }

    private int HoarePartition(T[] array, int start, int end)
    {
        T pivot = array[start];
        int i = start - 1;
        int j = end + 1;

        while(true)
        {
            do
            {
                i++;
            } while (array[i].compareTo(pivot) < 0);

            do
            {
                j--;
            } while (array[j].compareTo(pivot) > 0);
            if (i >= j) return j;
            Util.Swap(array, i, j);
        }
    }

    private void Sort(T[] array, int start, int end)
    {
        if(start < end)
        {
            int pivot = this.LomutoPartition(array, start, end);

            this.Sort(array, start, pivot - 1);
            this.Sort(array, pivot + 1, end);
        }
    }

    public void Sort(T[] array)
    {
        this.Sort(array, 0, array.length - 1);
    }
        
}


