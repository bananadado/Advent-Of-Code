using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day25
{
    internal class Day25
    {
        static List<List<char>> nums = new List<List<char>>();
        static void partToEndAllParts()
        {
            //decode and summate
            long total = 0;
            foreach (var item in nums)
            {
                long temptotal = 0;
                for (int i = 0; i < item.Count(); i++)
                {
                    if (item[i] == '=')
                    {
                        temptotal -= (long)Math.Pow(5, i) * 2;
                    }
                    else if (item[i] == '-')
                    {
                        temptotal -= (long)Math.Pow(5, i);
                    }
                    else
                    {
                        temptotal += (long)Math.Pow(5, i) * long.Parse(item[i].ToString());
                    }                    
                }
                total += temptotal;
            }
            Console.WriteLine(total);

            //encode
            List<char> SNAFU = new List<char>();
            while (total > 0)
            {
                int remainder = (int)(total % 5);
                total = total / 5;
                if (remainder < 3)
                {
                    SNAFU.Add(remainder.ToString()[0]);
                }
                else if (remainder == 3)
                {
                    SNAFU.Add('=');
                    total += 1; //a sort of carry over
                }
                else
                {
                    SNAFU.Add('-');
                    total += 1;
                }
            }
            SNAFU.Reverse();
            Console.WriteLine(new string(SNAFU.ToArray()));
        }
        static void Main(string[] args)
        {
            using(StreamReader sr = new StreamReader("input.txt"))
            {
                while (!sr.EndOfStream)
                {
                    char[] line = sr.ReadLine().ToCharArray();
                    List<char> line2 = line.ToList();
                    line2.Reverse();
                    nums.Add(line2);
                }
            }
            partToEndAllParts();
            Console.ReadKey();
        }
    }
}
