using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

//not a great solution this time
namespace Day10
{
    internal class Day10
    {
        static void Main(string[] args)
        {
            List<string> list = new List<string>();
            using (StreamReader sr = new StreamReader("input.txt"))
            {
                while (!sr.EndOfStream)
                {
                    list.Add(sr.ReadLine());
                }
            }

            List<int> toCheck = new List<int>() { 20,60,100,140,180,220};
            int cycle = 0;
            int X = 1;
            int total = 0;

            Char[ , ] CRT = new char[6,40];
            for (int i = 0; i < 6; i++)
            {
                for (int j = 0; j < 40; j++)
                {
                    CRT[i, j] = '.';
                }
            }

            foreach(string command in list)
            {
                if (command == "noop")
                {
                    cycle++;
                }
                else
                {
                    cycle++;
                    if (X + 2 > cycle % 40 - 1 && X - 2 < cycle % 40 - 1)
                    {
                        if (cycle > 200)
                        {
                            try
                            {
                                CRT[5, cycle % 40 - 1] = '#';
                            }
                            catch (Exception)
                            {
                                CRT[5, 39] = '#';
                            }
                        }
                        else if (cycle > 160)
                        {
                            try
                            {
                                CRT[4, cycle % 40 - 1] = '#';
                            }
                            catch (Exception)
                            {
                                CRT[4, 39] = '#';
                            }
                        }
                        else if (cycle > 120)
                        {
                            try
                            {
                                CRT[3, cycle % 40 - 1] = '#';
                            }
                            catch (Exception)
                            {
                                CRT[3, 39] = '#';
                            }
                        }
                        else if (cycle > 80)
                        {
                            try
                            {
                                CRT[2, cycle % 40 - 1] = '#';
                            }
                            catch (Exception)
                            {
                                CRT[2, 39] = '#';
                            }
                        }
                        else if (cycle > 40)
                        {
                            try
                            {
                                CRT[1, cycle % 40 - 1] = '#';
                            }
                            catch (Exception)
                            {
                                CRT[1, 39] = '#';
                            }
                        }
                        else
                        {
                            try
                            {
                                CRT[0, cycle % 40 - 1] = '#';
                            }
                            catch (Exception)
                            {
                                CRT[0, 39] = '#';
                            }
                        }
                    }

                    if (toCheck.Contains(cycle + 1))
                    {
                        total += X * (cycle + 1);
                    }

                    cycle++;
                }
                if (X + 2 > cycle % 40 - 1 && X - 2 < cycle % 40 - 1)
                {
                    if (cycle > 200)
                    {
                        try
                        {
                            CRT[5, cycle % 40 - 1] = '#';
                        }
                        catch (Exception)
                        {
                            CRT[5, 39] = '#';
                        }
                    }
                    else if (cycle > 160)
                    {
                        try
                        {
                            CRT[4, cycle % 40 - 1] = '#';
                        }
                        catch (Exception)
                        {
                            CRT[4, 39] = '#';
                        }
                    }
                    else if (cycle > 120)
                    {
                        try
                        {
                            CRT[3, cycle % 40 - 1] = '#';
                        }
                        catch (Exception)
                        {
                            CRT[3, 39] = '#';
                        }
                    }
                    else if (cycle > 80)
                    {
                        try
                        {
                            CRT[2, cycle % 40 - 1] = '#';
                        }
                        catch (Exception)
                        {
                            CRT[2, 39] = '#';
                        }
                    }
                    else if (cycle > 40)
                    {
                        try
                        {
                            CRT[1, cycle % 40 - 1] = '#';
                        }
                        catch (Exception)
                        {
                            CRT[1, 39] = '#';
                        }
                    }
                    else
                    {
                        try
                        {
                            CRT[0, cycle % 40 - 1] = '#';
                        }
                        catch (Exception)
                        {
                            CRT[0, 39] = '#';
                        }
                    }
                }
                if (command != "noop")
                {                    
                    X += int.Parse(command.Split(' ')[1]);
                }
                if (toCheck.Contains(cycle + 1))
                {
                    total += X * (cycle + 1);
                }
            }
            Console.WriteLine("Part 1: " + total);
            Console.WriteLine("Part 2:");
            for (int i = 0; i < 6; i++)
            {
                for (int j = 0; j < 40; j++)
                {
                    Console.Write(CRT[i, j]);
                }
                Console.WriteLine();
            }
            Console.ReadKey();
        }
    }
}
