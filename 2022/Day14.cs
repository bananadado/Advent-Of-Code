using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Runtime.CompilerServices;

namespace Day14
{
    internal class Day14
    {
        //in testing i found that my array had somehow roatated and flipped the rock formation, i accounted for this
        static List<List<string>> rocks = new List<List<string>>();
        static char[,] cave = new char[500, 201];

        static void populateArray()
        {
            for (int i = 0; i < cave.GetLength(0); i++)
            {
                for (int j = 0; j < cave.GetLength(1); j++)
                {
                    cave[i,j] = '.';
                }
            }
            for (int i = 0; i < rocks.Count(); i++)
            {
                int prevX = int.Parse(rocks[i][0].Split(',')[0]) - 250;
                int prevY = int.Parse(rocks[i][0].Split(',')[1]);
                for (int j = 0; j < rocks[i].Count(); j++)
                {
                    
                    int x = int.Parse(rocks[i][j].Split(',')[0])-250;
                    int y = int.Parse(rocks[i][j].Split(',')[1]);

                    //Console.WriteLine(x + " " + y);
                    if (prevX == x && prevY == y)
                    {
                        cave[x,y] = '#';
                    }
                    else if (prevX == x)
                    {
                        if (prevY > y)
                        {
                            for (int k = prevY; k >= y; k--)
                            {
                                cave[x, k] = '#';
                            }
                        }
                        else
                        {
                            for (int k = prevY; k <= y; k++)
                            {
                                cave[x, k] = '#';
                            }
                        }
                    }
                    else
                    {
                        if (prevX > x)
                        {
                            for (int k = prevX; k >= x; k--)
                            {
                                cave[k, y] = '#';
                            }
                        }
                        else
                        {
                            for (int k = prevX; k <= x; k++)
                            {
                                cave[k, y] = '#';
                            }
                        }
                    }

                    prevX = int.Parse(rocks[i][j].Split(',')[0]) - 250;
                    prevY = int.Parse(rocks[i][j].Split(',')[1]);

                }
            }
            int ycount = 0;

            for (int i = 0; i < cave.GetLength(0); i++)
            {
                for (int j = 0; j < cave.GetLength(1); j++)
                {
                    if (cave[i, j] == '#' && j>ycount)
                    {
                        ycount = j;
                    }
                }
            }
            for (int i = 0; i < 500; i++)
            {
                cave[i, ycount + 2] = '#';
            }
        }

        static void addSand()
        {
            bool found = false;
            for (int i = 0; i < 500*200; i++)
            {
                (int x, int y) sand = (250, 0);

                while (true)
                {
                    
                    if (cave[sand.x,sand.y + 1] == '.')
                    {
                        sand.y++;
                    }
                    else if (cave[sand.x - 1, sand.y + 1] == '.')
                    {
                        sand.x--;
                        sand.y++;
                    }
                    else if (cave[sand.x + 1, sand.y + 1] == '.')
                    {
                        sand.x++;
                        sand.y++;
                    }
                    else
                    {
                        cave[sand.x, sand.y] = 'o';
                        if (sand.y == 0 && sand.x == 250)//part 1 is the same but this if statemnt is directly under the while(true) and checks for if y = 200. Also the last 2 for loops in populate are removed
                        {
                            Console.WriteLine(i+1);
                            found = true;                            
                        }
                        break;
                    }                    
                }
                if (found)
                {
                    break;
                }
            }
        }

        static void Main(string[] args)
        {
            using(StreamReader sr = new StreamReader("input.txt"))
            {
                while (!sr.EndOfStream)
                {
                    rocks.Add(sr.ReadLine().Split(new[] { " -> " }, StringSplitOptions.None).ToList());
                }
            }

            populateArray();
            addSand();

            Console.ReadKey();
        }
    }
}
