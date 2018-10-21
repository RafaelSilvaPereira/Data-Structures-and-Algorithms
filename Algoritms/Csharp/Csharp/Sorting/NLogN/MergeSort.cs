using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Csharp.Sorting.NLogN
{
    class MergeSort<T> where T: IComparable<T>
    {
        private void Merge(T[] array, int start, int middle, int end)
        {
            int arrayLength = array.Length;
            T[] copy = new T[arrayLength];
            System.Array.Copy(array, copy, arrayLength);

            int indexA = start;
            int indexB = middle + 1;

            int indexK = start;

            while (indexA <= middle &&  indexB <= end)
            {
                if (copy[indexA].CompareTo(copy[indexB]) < 0)
                {
                    array[indexK++] = copy[indexA++];
                }
                else
                {
                    array[indexK++] = copy[indexB++];
                }

            }

         

            while(indexA <= middle)
            {
                array[indexK++] = copy[indexA++];
             }

        while(indexB <= end)
            {
                array[indexK++] = copy[indexB++];
            }
        }


        public void Sort(T[] array)
        {
            this.Sort(array, 0, array.Length - 1);
        }

        private void Sort(T[] array, int start, int end)
        {
           if(start < end)
            {
                int middle = (start + end) / 2;

                this.Sort(array, start, middle);
                this.Sort(array, middle + 1, end);

                this.Merge(array, start, middle, end);

            }
        }
    }
}
