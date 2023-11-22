using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day3
{
    internal class Day03
    {
        static void Main(string[] args)
        {
            int total = 0;
            using (StreamReader sr = new StreamReader("input.txt"))
            {
                while (!sr.EndOfStream)
                {
                    string line = sr.ReadLine();
                    char[] first = line.Substring(0, line.Length/2).ToCharArray();
                    char[] last = line.Substring(line.Length/2).ToCharArray();
                    char ch = first.Intersect(last).ToList()[0];
                    
                    if (Char.IsUpper(ch))
                    {
                        total += (int)ch - 38;
                    }
                    else
                    {
                        total += (int)ch - 96;
                    }

                }
            }
            Console.WriteLine("Part 1: "+total);

            total = 0;
            using(StreamReader sr = new StreamReader("input.txt"))
            {
                char ch = 'E'; //random character assigned as visual studio didn't like it
                while (!sr.EndOfStream)
                {
                    string line1 = sr.ReadLine();
                    string line2 = sr.ReadLine();
                    string line3 = sr.ReadLine();
                    
                    foreach (char c in line1)
                    {
                        if (line2.Contains(c) && line3.Contains(c)) 
                        {
                            ch = c;
                            break;
                        }
                    }
                    if (Char.IsUpper(ch))
                    {
                        total+= (int)ch - 38;
                    }
                    else
                    {
                        total += (int)ch - 96;
                    }
                    
                }
            }
            Console.WriteLine("Part 2: "+total);
            Console.ReadKey();
        }
    }
}
