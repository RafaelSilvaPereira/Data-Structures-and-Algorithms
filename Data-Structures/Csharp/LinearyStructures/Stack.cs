using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LinearyStructures
{
    class Stack<T> where T: IComparable
    {
        private int top;
        private List<T> array;

        public Stack()
        {
            this.top = -1;
            this.array = new List<T>();
        }

        public void Push(T element)
        {
            if(!element.Equals(default(T)) && element != null)
            {
                this.array.Insert(this.top++, element);
            }
        }


        public T Pop()
        {
            T ans = default(T);
            if(!this.IsEmpty())
            {
                ans = this.array.ElementAt(this.top);
                this.array.RemoveAt(this.top--);
            } else
            {
                throw new StackUnderflowException();
            }
            return ans;
        }

        public T Top()
        {
            return this.array.ElementAt(this.top);
        }

        public int Elements()
        {
            return this.top + 1;
        }

        private bool IsEmpty()
        {
            return this.array.Count() == 0;
        }
    }
}
