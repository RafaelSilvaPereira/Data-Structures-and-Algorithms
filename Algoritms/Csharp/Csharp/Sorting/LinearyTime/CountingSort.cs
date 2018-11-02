﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Csharp.Sorting.LinearyTime
{
    public class CountingSort
    {
        public CountingSort()
        {

        }

        public void Sort(int[] array)
        {
            int smaller = array.Min();
            int keyValue = 0;
            if (smaller < 0) keyValue = 1 - smaller;

            int lenArray = array.Count();
            int[] tempArray = new int[lenArray];

            for (int i = 0; i < lenArray; i++) tempArray[i] = array[i] + keyValue;

            int bigger = tempArray.Max();
            smaller = tempArray.Min();
            int size = (bigger - smaller) + 2;

            int[] contArray = new int[size];

            for (int i = 0; i < tempArray.Count(); i++) contArray[tempArray[i] - smaller + 1]++;
            for (int i = 1; i < contArray.Count(); i++) contArray[i] += contArray[i - 1];

            for (int i = 0; i < lenArray; i++)
            {
                array[contArray[tempArray[i] - smaller + 1] - 1] = tempArray[i];
                contArray[tempArray[i] - smaller + 1]--;
            }        
        }
    }
}
