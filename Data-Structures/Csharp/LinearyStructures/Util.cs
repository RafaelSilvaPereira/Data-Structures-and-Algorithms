using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LinearyStructures
{
    class Util
    {

        public static void Swap<T>(T[] collection, int indexA, int indexB)
        {
            T obj = collection[indexA];
            collection[indexA] = collection[indexB];
            collection[indexB] = obj;
        }


        public static String ArraysToString<T>(T[] array)
        {
            return string.Join(", ", array);
        }
    }
}
