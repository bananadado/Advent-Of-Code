using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Runtime.Serialization.Formatters;

namespace Day8
{
    internal class Day08
    {
        static void Main(string[] args)
        {
            List<List<int>> input = new List<List<int>>();
            using(StreamReader sr = new StreamReader("input.txt"))
            {
                while (!sr.EndOfStream)
                {
                    List<int> ints = new List<int>();
                    char[] numbers = sr.ReadLine().ToCharArray();
                    foreach (char c in numbers)
                    {
                        ints.Add(int.Parse(c.ToString()));
                    }
                    input.Add(ints);
                }
            }



            int highest = 0;
            int visible = 0;

            for (int i =0; i < input.Count; i++)
            {
                for (int j = 0; j < input[i].Count; j++)
                {
                    if (i == 0 || j == 0 || i == input[i].Count - 1 || j == input.Count() - 1)
                    {
                        visible++;
                        continue;
                    }
                    else
                    {
                        //part 1
                        bool invisible = true;
                        for (int z = 0; z < 1; z++)//loop so that I can break out of it while still being able to do part 2, written post solve so thats why its a bit long lol
                        {
                            for (int k = i - 1; k >= 0; k--)//up
                            {
                                if (!(input[k][j] < input[i][j]))
                                {
                                    break;
                                }
                                if (k == 0)
                                {
                                    visible++;
                                    invisible = false;
                                }
                            }
                            if (!invisible) { break; }

                            for (int k = i + 1; k < input.Count(); k++)//down
                            {
                                if (!(input[k][j] < input[i][j]))
                                {
                                    break;
                                }
                                if (k == input.Count() - 1)
                                {
                                    visible++;
                                    invisible = false;
                                }
                            }
                            if (!invisible) { break; }

                            for (int k = j - 1; k >= 0; k--)//left
                            {
                                if (!(input[i][k] < input[i][j]))
                                {
                                    break;
                                }
                                if (k == 0)
                                {
                                    visible++;
                                    invisible = false;
                                }
                            }
                            if (!invisible) { break; }

                            for (int k = j + 1; k < input[i].Count(); k++)//right
                            {
                                if (!(input[i][k] < input[i][j]))
                                {
                                    break;
                                }
                                if (k == input[i].Count() - 1)
                                {
                                    visible++;
                                }
                            }
                        }

                        //part 2
                        int LH = 0;
                        int RH = 0;
                        int TH = 0;
                        int BH = 0;
                        for (int k = i - 1; k >= 0; k--)//up
                        {
                            if (input[k][j] < input[i][j])
                            {
                                TH++;
                            }
                            else
                            {
                                TH++;
                                break;
                            }
                        }
                        for (int k = i + 1; k < input.Count(); k++)//down
                        {
                            if (input[k][j] < input[i][j])
                            {
                                BH++;
                            }
                            else
                            {
                                BH++;
                                break;
                            }
                        }
                        for (int k = j - 1; k >= 0; k--)//left
                        {
                            if (input[i][k] < input[i][j])
                            {
                                LH++;
                            }
                            else
                            {
                                LH++;
                                break;
                            }
                        }
                        for (int k = j + 1; k < input[i].Count(); k++)//right
                        {
                            if (input[i][k] < input[i][j])
                            {
                                RH++;
                            }
                            else
                            {
                                RH++;
                                break;
                            }
                        }
                        if (RH*LH*BH*TH > highest)
                        {
                            highest = RH * LH * BH * TH;
                        }
                    }
                }
            }
            Console.WriteLine("Part 1: " + visible);
            Console.WriteLine("Part 2: " + highest);
            Console.ReadKey();
        }
    }
}
