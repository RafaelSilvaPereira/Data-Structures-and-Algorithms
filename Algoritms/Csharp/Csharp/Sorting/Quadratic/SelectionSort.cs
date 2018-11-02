using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Csharp.Sorting;

namespace Csharp.Sorting.Quadratic
{

    public class SelectionSort<T> where T : IComparable<T>
    {

        private int SelectSmaller(T[] array, int startIndex, int endIndex)
        {
            int SmallerIndex = startIndex;

            for (int i = startIndex; i < endIndex; i++)
            {
                if (array[i].CompareTo(array[SmallerIndex]) < 0)
                {
                    SmallerIndex = i;
                }
            }
            return SmallerIndex;
        }

        public void Sort(T[] array)
        {
            int arrayLength = array.Length;
            for (int i = 0; i < arrayLength; i++)
            {
                int indexSmaller = SelectSmaller(array, i, arrayLength);
                Util.Swap(array, i, indexSmaller);
            }
        }
    }
    }
