using System;
using System.Collections;
using System.Collections.Generic;
using System.Data;
using System.IO;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Day23
{
    internal class Program
    {
        static List<List<char>> map = new List<List<char>>();
        static Dictionary<(int, int), (int, int)> movement = new Dictionary<(int, int), (int, int)>();//coordinate to go, coordinate to delete
        static List<(int, int)> cantMove = new List<(int, int)>();
        static bool north((int row, int column) coord)
        {
            if (map[coord.row - 1][coord.column - 1] == '.' && map[coord.row - 1][coord.column] == '.' && map[coord.row - 1][coord.column+1] == '.')
            {
                if (movement.ContainsKey((coord.row - 1, coord.column)))
                {
                    cantMove.Add((coord.row - 1, coord.column));
                }
                else
                {
                    movement.Add((coord.row - 1, coord.column), coord);
                }
                return true;
            }
            return false;
        }
        static bool south((int row, int column) coord)
        {
            if (map[coord.row + 1][coord.column - 1] == '.' && map[coord.row + 1][coord.column] == '.' && map[coord.row + 1][coord.column + 1] == '.')
            {
                if (movement.ContainsKey((coord.row + 1, coord.column)))
                {
                    cantMove.Add((coord.row + 1, coord.column));
                }
                else
                {
                    movement.Add((coord.row + 1, coord.column), coord);
                }
                return true;
            }
            return false;
        }
        static bool west((int row, int column) coord)
        {
            if (map[coord.row - 1][coord.column - 1] == '.' && map[coord.row][coord.column-1] == '.' && map[coord.row + 1][coord.column - 1] == '.')
            {
                if (movement.ContainsKey((coord.row, coord.column-1)))
                {
                    cantMove.Add((coord.row, coord.column - 1));
                }
                else
                {
                    movement.Add((coord.row, coord.column - 1), coord);
                }
                return true;
            }
            return false;
        }
        static bool east((int row, int column) coord)
        {
            if (map[coord.row + 1][coord.column + 1] == '.' && map[coord.row][coord.column + 1] == '.' && map[coord.row - 1][coord.column + 1] == '.')
            {
                if (movement.ContainsKey((coord.row, coord.column - 1)))
                {
                    cantMove.Add((coord.row, coord.column + 1));
                }
                else
                {
                    movement.Add((coord.row, coord.column + 1), coord);
                }
                return true;
            }
            return false;
        }

        static void part1()
        {
            for (int i = 0; i < 10; i++)           
            {
                int count = 0;
                //iterate through the map
                for (int j = 0; j < map.Count(); j++)
                {
                    for (int k = 0; k < map[j].Count(); k++)
                    {
                        if (map[j][k] == '#')
                        {
                            if (map[j - 1][k-1] == '.' && map[j][k-1] == '.' && map[j + 1][k - 1] == '.' && map[j + 1][k] == '.' && map[j + 1][k + 1] == '.' && map[j][k + 1] == '.' && map[j - 1][k + 1] == '.' && map[j - 1][k] == '.')
                            {
                                continue;
                            }
                            switch (i % 4)
                            {
                                case 0:
                                    if (north((j, k))) { break; }
                                    if (south((j, k))) { break; }
                                    if (west((j, k))) { break; }
                                    if (east((j, k))) { break; }
                                    break;
                                case 1:
                                    if (south((j, k))) { break; }
                                    if (west((j, k))) { break; }
                                    if (east((j, k))) { break; }
                                    if (north((j, k))) { break; }
                                    break;
                                case 2:
                                    if (west((j, k))) { break; }
                                    if (east((j, k))) { break; }
                                    if (north((j, k))) { break; }
                                    if (south((j, k))) { break; }
                                    break;
                                case 3:
                                    if (east((j, k))) { break; }
                                    if (north((j, k))) { break; }
                                    if (south((j, k))) { break; }
                                    if (west((j, k))) { break; }
                                    break;
                            }
                            count++;
                        }
                    }
                }
                foreach (KeyValuePair<(int newx, int newy), (int oldx, int oldy)> entry in movement)
                {
                    if (cantMove.Contains(entry.Key)) { continue; }
                    map[entry.Key.newx][entry.Key.newy] = '#';
                    map[entry.Value.oldx][entry.Value.oldy] = '.';
                }
                movement.Clear();
                cantMove.Clear();
            }
            
            int startrow = 0;
            int endrow = 0;
            int startcol = 0;
            int endcol = 0;

            for (int i = 0; i < map.Count(); i++)
            {
                if (map[i].Contains('#'))
                {
                    startrow = i;
                    break;
                }
            }
            for (int i = map.Count()-1; i >= 0; i--)
            {
                if (map[i].Contains('#'))
                {
                    endrow = i;
                    break;
                }
            }
            bool canbreak = false;
            for (int i = 0; i < map.Count(); i++)
            {
                for (int j = 0; j < map.Count(); j++)
                {
                    if (map[j][i] == '#')
                    {
                        startcol = i;
                        canbreak = true;
                        break;
                    }
                }
                if (canbreak)
                {
                    break;
                }
            }
            canbreak = false;
            for (int i = map.Count()-1; i >= 0; i--)
            {
                for (int j = 0; j < map.Count(); j++)
                {
                    if (map[j][i] == '#')
                    {
                        endcol = i;
                        canbreak = true;
                        break;
                    }
                }
                if (canbreak)
                {
                    break;
                }
            }
            using (StreamWriter sw = new StreamWriter("cry.txt"))
            {
                foreach (var item in map)
                {
                    foreach (var item1 in item)
                    {
                        sw.Write(item1);
                    }
                    sw.WriteLine();
                }
            }
            Console.WriteLine(startrow + " "+endrow + "  "+startcol + " " +endcol);

            int total = 0;
            for (int i = startrow; i <= endrow ; i++)
            {
                for (int j = startcol; j <= endcol; j++)
                {
                    if (map[i][j] == '.')
                    {
                        total++;
                    }
                }
            }
            Console.WriteLine("Part 1: "+total);
        }


        //part 2, please ignore the array solution to part 1
        static List<(int, int)> coordinates = new List<(int, int)>();
        static Dictionary<(int, int), (int, int)> movement2 = new Dictionary<(int, int), (int, int)>();
        static List<(int, int)> seen = new List<(int, int)>();

        static bool north2((int column, int row) coord)
        {
            if (!coordinates.Contains((coord.column - 1, coord.row - 1)) && !coordinates.Contains((coord.column, coord.row - 1)) && !coordinates.Contains((coord.column + 1, coord.row - 1)))
            {
                if (movement2.ContainsKey((coord.column, coord.row - 1)))
                {
                    seen.Add((coord.column, coord.row - 1));
                }
                else
                {
                    movement2.Add((coord.column, coord.row - 1), coord);
                }
                return true;
            }
            return false;
        }
        static bool south2((int column, int row) coord)
        {
            if (!coordinates.Contains((coord.column - 1, coord.row + 1)) && !coordinates.Contains((coord.column, coord.row + 1)) && !coordinates.Contains((coord.column + 1, coord.row + 1)))
            {
                if (movement2.ContainsKey((coord.column, coord.row + 1)))
                {
                    seen.Add((coord.column, coord.row + 1));
                }
                else
                {
                    movement2.Add((coord.column, coord.row + 1), coord);
                }
                return true;
            }
            return false;
        }
        static bool west2((int column, int row) coord)
        {
            if (!coordinates.Contains((coord.column - 1, coord.row - 1)) && !coordinates.Contains((coord.column - 1, coord.row )) && !coordinates.Contains((coord.column - 1, coord.row + 1)))
            {
                if (movement2.ContainsKey((coord.column - 1, coord.row)))
                {
                    seen.Add((coord.column - 1, coord.row));
                }
                else
                {
                    movement2.Add((coord.column - 1, coord.row ), coord);
                }
                return true;
            }
            return false;
        }
        static bool east2((int column, int row) coord)
        {
            if (!coordinates.Contains((coord.column + 1, coord.row - 1)) && !coordinates.Contains((coord.column + 1, coord.row)) && !coordinates.Contains((coord.column + 1, coord.row + 1)))
            {
                if (movement2.ContainsKey((coord.column + 1, coord.row)))
                {
                    seen.Add((coord.column + 1, coord.row));
                }
                else
                {
                    movement2.Add((coord.column + 1, coord.row), coord);
                }
                return true;
            }
            return false;
        }


        static void part2()
        {
            int l = 0;
            while(true)
            {
                int count = 0;
                //iterate through the map
                for (int j = 0; j < coordinates.Count(); j++)
                {
                    (int x, int y) = coordinates[j];
                    if (!coordinates.Contains(( x + 1, y)) && !coordinates.Contains((x+1, y + 1)) && !coordinates.Contains((x , y + 1)) && !coordinates.Contains((x - 1, y + 1)) && !coordinates.Contains((x - 1, y)) && !coordinates.Contains((x - 1, y - 1)) && !coordinates.Contains((x, y - 1)) && !coordinates.Contains((x + 1, y - 1)))
                    {
                        continue;
                    }
                    switch(l%4)
                    {
                        case 0:
                            if (north2((x, y))){ break; }
                            if (south2((x, y))){ break; }
                            if (west2((x, y))){ break; }
                            if (east2((x, y))){ break; }
                            break;
                        case 1:
                            if (south2((x, y))) { break; }
                            if (west2((x, y))) { break; }
                            if (east2((x, y))) { break; }
                            if (north2((x, y))) { break; }
                            break;
                        case 2:
                            if (west2((x, y))) { break; }
                            if (east2((x, y))) { break; }
                            if (north2((x, y))) { break; }
                            if (south2((x, y))) { break; }
                            break;
                        case 3:
                            if (east2((x, y))) { break; }
                            if (north2((x, y))) { break; }
                            if (south2((x, y))) { break; }
                            if (west2((x, y))) { break; }
                            break;
                    }
                    count++;
                }

                foreach (KeyValuePair<(int newx, int newy), (int oldx, int oldy)> entry in movement2)
                {
                    if (seen.Contains(entry.Key)) { continue; }                   
                    coordinates[coordinates.IndexOf(entry.Value)] = entry.Key;                    
                }
                movement2.Clear();
                seen.Clear();
                l++;
                
                if (count == 0)
                {
                    Console.WriteLine("Part 2: "+l);
                    break;
                }

            }

        }


        static void Main(string[] args)
        {
            using (StreamReader sr = new StreamReader("input.txt"))
            {
                map.Add((new string('~', 1000)).ToCharArray().ToList());
                while (!sr.EndOfStream)
                {
                    string line = sr.ReadLine();
                    List<char> bob = new string('.', 499 - line.Length / 2).ToCharArray().ToList();
                    bob.Insert(0, '~');
                    bob.AddRange(line.ToCharArray().ToList());
                    bob.AddRange(new string('.', 998 - bob.Count()).ToCharArray().ToList());
                    bob.Add('~');
                    map.Add(bob);
                }
                map.Add((new string('~', 1000)).ToCharArray().ToList());
            }
            for (int _ = 0; _ < (998 - map.Count()) / 2; _++)
            {
                map.Insert(1, (new string('.', 10000)).ToCharArray().ToList());
            }
            for (int _ = 0; _ < 998 - map.Count(); _++)
            {
                map.Insert(map.Count - 1, (new string('.', 1000)).ToCharArray().ToList());
            }

            part1();


            //part 2 using a more efficient method because part 1 is basically just a way of visualisation
            using (StreamReader sr  = new StreamReader("input.txt"))
            {
                int count = 0;
                while (!sr.EndOfStream)
                {
                    char[] line = sr.ReadLine().ToCharArray();
                    for (int i = 0; i < line.Length; i++)
                    {
                        if (line[i] == '#')
                        {
                            coordinates.Add((i, count));
                        }
                    }
                    count++;
                }
            }

            part2();

            Console.ReadKey();
        }
    }
}
