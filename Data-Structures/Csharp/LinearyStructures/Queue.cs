using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LinearyStructures
{
    class Queue<T> where T: IComparable
    {
        private List<T> array;

        public Queue()
        {
            this.array = new List<T>();
        }
        

       private bool isEmpty()
        {
            return this.array.Count() == 0;
        }

        public T Peek()
        {
            T ans = default(T);
            if (!this.isEmpty())
            {
                ans = this.array.ElementAt(0);
            }
            return ans;
        }

        public T Poll()
        {
            T ans = this.Peek();
            if (!ans.Equals(default(T)))
            { 
                this.array.RemoveAt(0); //remove the first element in to collention and aplicates a left shift
            }
        return ans;
        }


        public void Add(T element)
        {
            this.array.Add(element);
        }
    }
}
