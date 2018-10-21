using System;


namespace Csharp.Sorting
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
