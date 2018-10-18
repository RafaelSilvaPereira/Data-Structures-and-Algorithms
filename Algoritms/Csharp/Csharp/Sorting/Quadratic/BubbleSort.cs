using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Csharp.Sorting;

namespace Csharp.Sorting.Quadratic
{
    public class BubbleSort<T> where T : IComparable<T>
    {




        public void Sort(T[] array)
        {
            for (int i = 0; i < array.Length; i++)
            {
                for (int j = 0; j < array.Length - 1; j++)
                {
                    if (array[j].CompareTo(array[j + 1]) >= 1)
                    {
                        Util.Swap(array, j, j + 1);
                    }
                }
            }
        }
    }
}
