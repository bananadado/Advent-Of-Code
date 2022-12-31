using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Runtime.CompilerServices;
using System.Security.Cryptography.X509Certificates;

namespace Day12
{
    internal class Day12
    {
        static void part1()
        {
            List<List<char>> list = new List<List<char>>();
            using (StreamReader sr = new StreamReader("input.txt"))
            {
                while (!sr.EndOfStream)
                {
                    char[] line = sr.ReadLine().ToCharArray();
                    list.Add(line.ToList());
                }
            }

            Queue<(int, int, int)> queue = new Queue<(int, int, int)>();
            List<(int, int)> visited = new List<(int, int)>();
            (int x, int y) destination = (0, 0);

            for (int i = 0; i < list.Count; i++)
            {
                for (int j = 0; j < list[i].Count; j++)
                {
                    if (list[i][j] == 'E')
                    {
                        destination.x = i;
                        destination.y = j;

                        list[i][j] = 'z';
                    }
                    else if (list[i][j] == 'S')
                    {
                        queue.Enqueue((0, i, j));

                        list[i][j] = 'a';
                    }
                }
            }

            //part 1
            while (true)
            {
                bool found = false;
                (int count, int x, int y) current = queue.Dequeue();
                List<(int, int)> toTest = new List<(int, int)>() { (current.x + 1, current.y), (current.x - 1, current.y), (current.x, current.y + 1), (current.x, current.y - 1) };

                foreach ((int x, int y) item in toTest)
                {
                    if (visited.Contains((item.x, item.y)))
                    {
                        continue;
                    }
                    else if (item.x < 0 || item.y < 0 || item.x >= list.Count || item.y >= list[0].Count)
                    {
                        continue;
                    }
                    else if (list[item.x][item.y] - list[current.x][current.y] > 1)
                    {
                        continue;
                    }

                    if (item.x == destination.x && item.y == destination.y)
                    {
                        Console.WriteLine("Part 1: "+ (current.count + 1));
                        found = true;
                        break;
                    }

                    queue.Enqueue((current.count + 1, item.x, item.y));
                    visited.Add((item.x, item.y));
                }

                if (found)
                {
                    break;
                }
            }

        }

        static void part2()
        {
            List<List<char>> list = new List<List<char>>();
            using (StreamReader sr = new StreamReader("input.txt"))
            {
                while (!sr.EndOfStream)
                {
                    char[] line = sr.ReadLine().ToCharArray();
                    list.Add(line.ToList());
                }
            }

            Queue<(int, int, int)> queue = new Queue<(int, int, int)>();
            List<(int, int)> visited = new List<(int, int)>();

            for (int i = 0; i < list.Count; i++)
            {
                for (int j = 0; j < list[i].Count; j++)
                {
                    if (list[i][j] == 'E')
                    {
                        queue.Enqueue((0, i, j));

                        list[i][j] = 'z';
                    }
                    else if (list[i][j] == 'S')
                    {
                        list[i][j] = 'a';
                    }
                }
            }

            //part 1
            while (true)
            {
                bool found = false;
                (int count, int x, int y) current = queue.Dequeue();
                List<(int, int)> toTest = new List<(int, int)>() { (current.x + 1, current.y), (current.x - 1, current.y), (current.x, current.y + 1), (current.x, current.y - 1) };

                foreach ((int x, int y) item in toTest)
                {
                    if (visited.Contains((item.x, item.y)))
                    {
                        continue;
                    }
                    else if (item.x < 0 || item.y < 0 || item.x >= list.Count || item.y >= list[0].Count)
                    {
                        continue;
                    }
                    else if (list[item.x][item.y] - list[current.x][current.y] < -1)
                    {
                        continue;
                    }

                    if (list[item.x][item.y] == 'a')
                    {
                        Console.WriteLine("Part 2: " + (current.count + 1));
                        found = true;
                        break;
                    }

                    queue.Enqueue((current.count + 1, item.x, item.y));
                    visited.Add((item.x, item.y));
                }

                if (found)
                {
                    break;
                }
            }
        }
        static void Main(string[] args)
        {
            part1();
            //part 2 is the same but slightly changed - work backwards until an 'a' is found
            //basically the same thing - I should've made a function for the bfs but oh well
            part2();

            Console.ReadKey();
        }
    }
}
