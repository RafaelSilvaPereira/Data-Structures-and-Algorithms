using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Csharp.Sorting.Quadratic;
using Csharp.Sorting.NLogN;
using Csharp.Sorting.LinearyTime;
using Csharp.Sorting;

namespace ClassTest
{
    [TestClass]
    public class AllSortingTest
    {
        private BubbleSort<int> bbs = new BubbleSort<int>();
        private InsertionSort<int> ins = new InsertionSort<int>();
        private SelectionSort<int> sns = new SelectionSort<int>();
        private QuickSort<int> qks = new QuickSort<int>();
        private MergeSort<int> mgs = new MergeSort<int>();
        private CountingSort cgs = new CountingSort();
        private int[] array = Util.RandomList(10000);


        public bool isOrdened(int[] array)
        {
            bool ans = true;

            for(int i = 1; i< array.Length; i++)
            {
                if(array[i] < array[i - 1])
                {
                    ans = false;
                    break;
                }
            }
            return ans;
        }

        


        [TestMethod]
        public void BubbleSortTest()
        {
            Assert.IsFalse(this.isOrdened(array));
            bbs.Sort(array);
            Assert.IsTrue(this.isOrdened(array));

        }

        [TestMethod]
        public void SelectionSortTest()
        {
            Assert.IsFalse(this.isOrdened(array));
            sns.Sort(array);
            Assert.IsTrue(this.isOrdened(array));

        }

        [TestMethod]
        public void InsertionSortTest()
        {
            Assert.IsFalse(this.isOrdened(array));
            ins.Sort(array);
            Assert.IsTrue(this.isOrdened(array));

        }

        [TestMethod]
        public void MergeSortTest()
        {
            Assert.IsFalse(this.isOrdened(array));
            mgs.Sort(array);
            Assert.IsTrue(this.isOrdened(array));

        }

        [TestMethod]
        public void QuickSortTest()
        {
            Assert.IsFalse(this.isOrdened(array));
            qks.Sort(array);
            Assert.IsTrue(this.isOrdened(array));

        }

        [TestMethod]
        public void CountingSortTest()
        {
            Assert.IsFalse(this.isOrdened(array));
            cgs.Sort(array);
            Assert.IsTrue(this.isOrdened(array));

        }
    }
}
