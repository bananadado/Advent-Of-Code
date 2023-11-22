using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Runtime.CompilerServices;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace Day18
{
    internal class Day18
    {
        static List<(int, int, int)> coords = new List<(int, int, int)> (); //x,y,z
        static List<(int, int, int)> seen = new List<(int, int, int)>();
        static List<(int, int, int)> inside = new List<(int, int, int)> ();
        static List<(int, int, int)> outside = new List<(int, int, int)> ();

        static bool doesHave((int x1, int y1, int z1) coord)
        {
            if (seen.Contains((coord.x1, coord.y1, coord.z1)))
            {
                return false;
            }
            return true;
        }
        static int total = 0;
        static void part1()
        {
            for (int i = 0; i < coords.Count(); i++)
            {
                (int x, int y, int z) = coords[i];

                if(doesHave((x, y, z)))
                {
                    if (doesHave((x + 1, y, z))){
                        total++;
                    }
                    else
                    {
                        total--;
                    }
                    if (doesHave((x - 1, y, z))){
                        total++;
                    }
                    else
                    {
                        total--;
                    }
                    if (doesHave((x, y+1, z))){
                        total++;
                    }
                    else
                    {
                        total--;
                    }
                    if (doesHave((x, y - 1, z)))
                    {
                        total++;
                    }
                    else
                    {
                        total--;
                    }
                    if (doesHave((x, y, z+1)))
                    {
                        total++;
                    }
                    else
                    {
                        total--;
                    }
                    if (doesHave((x, y, z-1)))
                    {
                        total++;
                    }
                    else
                    {
                        total--;
                    }
                }


                seen.Add((x, y, z));

            }
            Console.WriteLine(total);
        }
        static bool isInside((int x1, int y1, int z1) coord)
        {
            //originally I had a very similar method with just a bunch of if statements which ran wayyy slower
            //I had also checked inside the loop whether or not it was inside/outside which was also slower so I have neatened it up quite a bit.
            if (inside.Contains((coord.x1, coord.y1, coord.z1)))
            {
                return true;
            }
            if (outside.Contains((coord.x1, coord.y1, coord.z1)))
            {
                return false;
            }

            Queue<(int, int, int)> coordsToCheck = new Queue<(int, int, int)>();
            List<(int, int, int)> visited = new List<(int, int, int)>();
            coordsToCheck.Enqueue((coord.x1,coord.y1,coord.z1));
            while (coordsToCheck.Count() > 0)
            {
                (int x, int y, int z) = coordsToCheck.Dequeue();
                
                if (coords.Contains((x, y, z))) { continue; }
                if (visited.Contains((x, y, z))) { continue;  }
                visited.Add((x, y, z));

                if (coordsToCheck.Count() > 10000)
                {
                    foreach ((int x1, int y1, int z1) in visited)
                    {
                        outside.Add((x1, y1, z1));
                    }
                    return false;
                }

                coordsToCheck.Enqueue((x + 1, y, z));
                coordsToCheck.Enqueue((x - 1, y, z));
                coordsToCheck.Enqueue((x, y + 1, z));
                coordsToCheck.Enqueue((x, y - 1, z));
                coordsToCheck.Enqueue((x, y, z - 1));
                coordsToCheck.Enqueue((x, y, z + 1));
            }
            foreach ((int x1, int y1, int z1) in visited)
            {
                inside.Add((x1, y1, z1));
            }
            return true;
        }
        static void part2()
        {
            for (int i = 0; i < coords.Count(); i++)
            {
                (int x, int y, int z) = coords[i];

                if (isInside((x + 1, y, z)) && !seen.Contains((x + 1, y, z)))
                {
                    total--;
                }
                if (isInside((x - 1, y, z)) && !seen.Contains((x - 1, y, z)))
                {
                    total--;
                }
                if (isInside((x, y + 1, z)) && !seen.Contains((x, y+1, z)))
                {
                    total--;
                }
                if (isInside((x, y - 1, z)) && !seen.Contains((x, y-1, z)))
                {
                    total--;
                }
                if (isInside((x, y, z + 1)) && !seen.Contains((x, y, z+1)))
                {
                    total--;
                }
                if (isInside((x, y, z - 1)) && !seen.Contains((x, y, z -1)))
                {
                    total--;
                }

                seen.Add((x, y, z));
            }
            Console.WriteLine(total);
        }
        static void Main(string[] args)
        {
            List<List<int>> input = new List<List<int>>();
            using (StreamReader sr = new StreamReader("input.txt"))
            {
                while (!sr.EndOfStream)
                {
                    string[] line = sr.ReadLine().Split(',');
                    List<int> temp = new List<int>();
                    foreach (string line2 in line)
                    {
                        temp.Add(int.Parse(line2));
                    }
                    input.Add(temp);
                }
            }
            foreach (List<int> list in input)
            {
                (int x, int y, int z) coord;

                coord.x = list[0];
                coord.y = list[1];
                coord.z = list[2];
                coords.Add(coord);
            }
            part1();
            part2();
            Console.ReadKey();
        }
    }
}
