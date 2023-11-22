using System;
using System.Collections.Generic;
using System.Data.Odbc;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//could have easily made one subroutine but for some reason i did a copypasta for part 2????
namespace Day24
{
    internal class Day24
    {
        static int width;
        static int height;
        static List<(int, int)> blizzards = new List<(int, int)>();
        static List<char> directions = new List<char>();
        static Queue<(int, int )> players = new Queue<(int, int)>();
        static int count = 0;

        static void moveBlizzards()
        {
            for (int i = 0; i < blizzards.Count(); i++)
            {
                (int column, int row) = blizzards[i];
                switch (directions[i])
                {
                    case '^':
                        row--;
                        if (row == 0)
                        {
                            row = height - 2;
                        }
                        break;
                    case 'v':
                        row++;
                        if (row == height - 1)
                        {
                            row = 1;
                        }
                        break;
                    case '>':
                        column++;
                        if (column == width - 1)
                        {
                            column = 1;
                        }
                        break;
                    case '<':
                        column--;
                        if (column == 0)
                        {
                            column = width - 2;
                        }
                        break;
                }
                blizzards[i] = (column, row);
            }
        }
        static bool movePlayer()
        {
            List<(int, int)> tempplayers = new List<(int, int)>();
            while (players.Count() > 0)
            {
                (int column, int row) = players.Dequeue();

                if (row == height - 2  && column == width - 2)
                {
                    return false;
                }

                if (!tempplayers.Contains((column - 1, row)) && !blizzards.Contains((column - 1, row)) && column - 1 > 0 && row > 0 && row < height)
                {
                    tempplayers.Add((column - 1, row));
                }
                if (!tempplayers.Contains((column + 1, row)) && !blizzards.Contains((column + 1, row)) && column + 1 < width - 1 && row > 0 && row < height)
                {
                    tempplayers.Add((column + 1, row));
                }
                if (!tempplayers.Contains((column, row - 1)) && !blizzards.Contains((column, row - 1)) && row - 1 > 0 && column > 0 && column < width)
                {
                    tempplayers.Add((column, row - 1));
                }
                if (!tempplayers.Contains((column, row + 1)) && !blizzards.Contains((column , row + 1)) && row + 1 < height - 1 && column > 0 && column < width)
                {
                    tempplayers.Add((column, row + 1));
                }
                if (!tempplayers.Contains((column, row)) && !blizzards.Contains((column , row)))//wait
                {
                    tempplayers.Add((column, row));
                }
            }
            for (int i = 0; i < tempplayers.Count(); i++)
            {
                players.Enqueue(tempplayers[i]);
            }
            tempplayers.Clear();

            return true;
        }
        static bool movePlayerBack()
        {
            List<(int, int)> tempplayers = new List<(int, int)>();
            while (players.Count() > 0)
            {
                (int column, int row) = players.Dequeue();

                if (row == 1 && column == 1)
                {
                    return false;
                }

                if (!tempplayers.Contains((column - 1, row)) && !blizzards.Contains((column - 1, row)) && column - 1 > 0 && column - 1 < width - 1 && row > 0 && row < height - 1)
                {
                    tempplayers.Add((column - 1, row));
                }
                if (!tempplayers.Contains((column + 1, row)) && !blizzards.Contains((column + 1, row)) && column + 1 < width - 1 && column > 0 && row > 0 && row < height - 1)
                {
                    tempplayers.Add((column + 1, row));
                }
                if (!tempplayers.Contains((column, row - 1)) && !blizzards.Contains((column, row - 1)) && row - 1 > 0 && row - 1 < height - 1 && column > 0 && column < width)
                {
                    tempplayers.Add((column, row - 1));
                }
                if (!tempplayers.Contains((column, row + 1)) && !blizzards.Contains((column, row + 1)) && row + 1 < height - 1 && row > 0 && column > 0 && column < width)
                {
                    tempplayers.Add((column, row + 1));
                }
                if (!tempplayers.Contains((column, row)) && !blizzards.Contains((column, row)))//wait
                {
                    tempplayers.Add((column, row));
                }
            }
            for (int i = 0; i < tempplayers.Count(); i++)
            {
                players.Enqueue(tempplayers[i]);
            }
            tempplayers.Clear();

            return true;
        }
        static void part1()
        {
            players.Enqueue((1,0));
            bool True = true;
            while (True)
            {
                count++;
                moveBlizzards();
                True = movePlayer();
            }
            Console.WriteLine("Part 1: "+count);
        }
        static void part2()
        {
            bool True = true;
            players.Clear();
            count++;//Have to do this and the following command as I dont actually check the right coordinate
            moveBlizzards();
            players.Enqueue((width - 2, height - 1));
            while (True)
            {
                count++;
                moveBlizzards();
                True = movePlayerBack();

                //useful tool for checking the grid
                //for (int i = 0; i < height; i++)
                //{
                //    for (int j = 0; j < width; j++)
                //    {
                //        if (players.Contains((j, i)))
                //        {
                //            Console.Write('E');
                //        }
                //        else if (blizzards.Contains((j, i)))
                //        {
                //            Console.Write('^');
                //        }
                //        else
                //        {
                //            Console.Write('#');
                //        }
                //    }
                //    Console.WriteLine();
                //}
                //Console.WriteLine();
            }
            Console.WriteLine("Moved back: "+count);

            True = true;
            players.Clear();
            count++;
            moveBlizzards();
            players.Enqueue((1, 0));
            while (True)
            {
                count++;
                moveBlizzards();
                True = movePlayer();
            }
            Console.WriteLine("Part 2: "+count);
        }
        static void Main(string[] args)
        {
            using (StreamReader sr = new StreamReader("input.txt"))
            {
                int count = 0;
                while (!sr.EndOfStream)
                {
                    char[] line = sr.ReadLine().ToCharArray();
                    width = line.Length;
                    for (int i = 0; i < line.Length; i++)
                    {
                        if (line[i] != '.' && line[i] != '#')
                        {
                            blizzards.Add((i, count));
                            directions.Add(line[i]);
                        }
                        if (count>0 && i>0 && line[i] == '#' && line[i-1] == '#')
                        {
                            height = count + 1;
                        }
                    }
                    count++;
                }
            }

            part1();
            part2();
            Console.ReadKey();
        }
    }
}
