using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;

namespace Day1
{
    internal class Day01
    {
        static void Main(string[] args)
        {
            List<int> calories = new List<int>();

            //bit of a weird parse but oh well
            using (StreamReader sr = new StreamReader("input.txt"))
            {
                while (!sr.EndOfStream)
                {
                    int tempint = 0;
                    bool cando = true;
                    do
                    {
                        try
                        {
                            tempint += int.Parse(sr.ReadLine());
                        }
                        catch (Exception)
                        {
                            cando = false;
                        }

                    } while (cando);
                    calories.Add(tempint);
                }
            }

            Console.WriteLine("Part 1: "+calories.Max());

            calories.Sort();
            calories.Reverse();
            int totalhighest = calories[0] + calories[1] + calories[2];            
            Console.WriteLine("Part 2: "+totalhighest);
            Console.ReadKey();
        }
    }
}
