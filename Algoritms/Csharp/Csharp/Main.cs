using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Csharp.Sorting.Quadratic;
using Csharp.Sorting;
using Csharp.Sorting.NLogN;

namespace Csharp
{

    class main
    {
        static void Main(string[] args)
        {
            //BubbleSort<int> bb = new BubbleSort<int>();
            //SelectionSort<int> st = new SelectionSort<int>();
            //InsertionSort<int> it = new InsertionSort<int>();
            //MergeSort<int> mg = new MergeSort<int>();
            QuickSort<int> Qk = new QuickSort<int>();
            int[] a = Util.RandomList(10);
            int[] b = new int[a.Length];





            Qk.Sort(a);


            Console.WriteLine("[{0}]", Util.ArraysToString(a));

        }
    }
}
