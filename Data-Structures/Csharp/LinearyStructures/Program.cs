using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using LinearyStructures;

namespace LinearyStructures
{
    class Program
    {
        static void Main(string[] args)
        {

            List<int> a = new List<int>();

            a.Add(1); a.Add(1+1); a.Add(1+2); a.Add(1 + 3);

            a.ForEach(Console.WriteLine);
            a.RemoveAt(0);
            a.ForEach(Console.WriteLine);



        }
    }
}
