using System;
using System.Collections.Generic;

namespace Csharp.Sorting
{
    public class Util
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


        public static int[] RandomList(int range)
        {
           
            List<int> array = new List<int>();
            Random randInt = new Random();


            for (int i = 0; i < range; i++)
            {
                
                int randomValue = randInt.Next(-1000, 1000);
                array.Add(randomValue);
            }

            return array.ToArray();
        }


    }
}
