using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Csharp.Sorting.Quadratic;
using Csharp.Sorting; 


namespace Csharp
{
    class main
    {
        static void Main(string[] args)
        {
            //BubbleSort<int> bb = new BubbleSort<int>();
            //SelectionSort<int> st = new SelectionSort<int>();
            InsertionSort<int> it = new InsertionSort<int>();
            int[] a = { 5, 3, 6, 8, -1 };


            it.Sort(a);


            Console.WriteLine("[{0}]", Util.ArraysToString(a));
        }

    }
}
