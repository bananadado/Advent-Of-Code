using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Xml.Schema;

namespace Day4
{
    internal class Day04
    {
        
        static void Main(string[] args)
        {
            int overlap1 = 0;
            int overlap2 = 0;
            using (StreamReader sr = new StreamReader("input.txt"))
            {
                while (!sr.EndOfStream)
                {
                    string line = sr.ReadLine();
                    string[] parts = line.Split(',');

                    if ((int.Parse(parts[0].Split('-')[0]) <= int.Parse(parts[1].Split('-')[0]) && int.Parse(parts[0].Split('-')[1]) >= int.Parse(parts[1].Split('-')[1])) || (int.Parse(parts[0].Split('-')[0]) >= int.Parse(parts[1].Split('-')[0]) && int.Parse(parts[0].Split('-')[1]) <= int.Parse(parts[1].Split('-')[1])))
                    {
                        overlap1++;
                    }
                    if ((int.Parse(parts[0].Split('-')[0]) <= int.Parse(parts[1].Split('-')[0]) && int.Parse(parts[0].Split('-')[1]) >= int.Parse(parts[1].Split('-')[0]))|| int.Parse(parts[1].Split('-')[0])<=int.Parse(parts[0].Split('-')[0]) && int.Parse(parts[1].Split('-')[1])>= int.Parse(parts[0].Split('-')[0]))
                    {
                        overlap2++;
                    }
                }
            }
            Console.WriteLine("Part 1: "+overlap1);
            Console.WriteLine("Part 2: "+overlap2);
            Console.ReadKey();
        }
    }
}
