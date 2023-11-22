using System;
using System.Collections.Generic;
using System.Data.SqlTypes;
using System.IO;
using System.Linq;
using System.Reflection.Emit;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace Day6
{
    internal class Day06
    {
        static int find(string input, int marker)
        {
            int pos = 0;

            for (int i = marker - 1; i < input.Length; i++)
            {
                string sub = input.Substring(i - (marker - 1), marker);
                int count = 0;
                for (int j = 0; j < sub.Length; j++)
                {
                    for (int k = 0; k < sub.Length; k++)
                    {
                        if (sub[j] == sub[k] && k != j)
                        {
                            count++;
                        }
                    }
                }
                if (count == 0)
                {
                    pos = i + 1;
                    break;
                }

            }            
            return pos;
        }

        static void Main(string[] args)
        {
            string input = File.ReadAllText("input.txt");

            Console.WriteLine("Part 1: " + find(input, 4));
            Console.WriteLine("Part 2: " + find(input, 14));
            Console.ReadKey();
        }
    }
}
