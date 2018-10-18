using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Csharp.Sorting;

namespace Csharp.Sorting.Quadratic
{
    public class InsertionSort<T> where T : IComparable<T>
    {
        private void OrderlyInsertion(T[] array, int start, int end, int currentIndex)
        {
            for (int i = end; i >= start; i--)
            {
                if (array[currentIndex].CompareTo(array[i]) < 0)
                {
                    Util.Swap(array, currentIndex, i);
                    currentIndex = i;
                }
            }
        }


        public void Sort(T[] array)
        {
            for (int i = 0; i < array.Length - 1; i++)
            {
                OrderlyInsertion(array, 0, i, i + 1);
            }
        }
    }
}
