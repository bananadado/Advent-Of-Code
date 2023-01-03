using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day22
{
    internal class Day22
    {
        static List<List<char>> map = new List<List<char>>();
        static List<List<char>> mapCopy = new List<List<char>>();
        static List<string> commands = new List<string>();
        static Dictionary<(int, int, char), (int, int, char)> a2b = new Dictionary<(int, int, char), (int, int, char)>();//(coord1, movement), (coord2, movement)
        static List<char> possibleRotations = new List<char>() { 'r', 'd', 'l', 'u' };
        static char rotation = 'r';
        static (int, int) movement((int x, int y) coords, int move, char direction)
        {
            rotation = direction;
            switch (direction)
            {
                case 'r':
                    for (int i = 0; i < move; i++)
                    {
                        mapCopy[coords.y][coords.x] = '>';
                        coords.x++;
                        if (map[coords.y][coords.x] == '#')
                        {
                            coords.x--;
                            break;
                        }
                        if (map[coords.y][coords.x] == '~')
                        {
                            (int newx, int newy, char c) = a2b[(coords.x-1, coords.y, 'r')];
                            if (map[newy][newx] == '.')
                            {
                                coords.x = newx;
                                coords.y = newy;
                                return movement((coords), move - i - 1, possibleRotations[(possibleRotations.IndexOf(c)+2)%4]);
                            }
                            else
                            {
                                coords.x--;
                                break;
                            }
                            
                        }
                    }
                    break;
                case 'l':
                    for (int i = 0; i < move; i++)
                    {
                        mapCopy[coords.y][coords.x] = '<';
                        coords.x--;
                        if (map[coords.y][coords.x] == '#')
                        {
                            coords.x++;
                            break;
                        }
                        if (map[coords.y][coords.x] == '~')
                        {
                            (int newx, int newy, char c) = a2b[(coords.x+1, coords.y, 'l')];
                            if (map[newy][newx] == '.')
                            {
                                coords.x = newx;
                                coords.y = newy;
                                return movement((coords), move - i -1, possibleRotations[(possibleRotations.IndexOf(c) + 2) % 4]);
                            }
                            else
                            {
                                coords.x++;
                                break;
                            }
                        }
                    }
                    break;
                case 'u':
                    for (int i = 0; i < move; i++)
                    {
                        mapCopy[coords.y][coords.x] = '^';
                        coords.y--;
                        if (map[coords.y][coords.x] == '#')
                        {
                            coords.y++;
                            break;
                        }
                        if (map[coords.y][coords.x] == '~')
                        {
                            (int newx, int newy, char c) = a2b[(coords.x, coords.y+1, 'u')];
                            if (map[newy][newx] == '.')
                            {
                                coords.x = newx;
                                coords.y = newy;
                                return movement((coords), move - i -1 , possibleRotations[(possibleRotations.IndexOf(c) + 2) % 4]);
                            }
                            else
                            {
                                coords.y++;
                                break;
                            }
                        }
                    }
                    break;
                case 'd':
                    for (int i = 0; i < move; i++)
                    {
                        coords.y++;
                        if (map[coords.y][coords.x] == '#')
                        {
                            coords.y--;
                            break;
                        }
                        if (map[coords.y][coords.x] == '~')
                        {
                            (int newx, int newy, char c) = a2b[(coords.x, coords.y-1, 'd')];
                            if (map[newy][newx] == '.')
                            {
                                coords.x = newx;
                                coords.y = newy;
                                return movement((coords), move - i -1 , possibleRotations[(possibleRotations.IndexOf(c) + 2) % 4]);
                            }
                            else
                            {
                                coords.y--;
                                break;
                            }
                        }
                    }
                    break;
            }
            return coords;
        }
        static void part1()
        {
            
            
            int move = int.Parse(commands[0]);
            (int x, int y) coords = (0,1);
            //find initial starting point
            coords.y = 1;
            for (int i = 0; i < map[1].Count(); i++)
            { 
                if (map[1][i] == '.')
                {
                    coords.x = i;
                    break;
                }
            }
            coords = movement(coords, move, rotation);
            for (int i = 1; i < commands.Count(); i++)
            {
                int num;
                switch (commands[i][0])
                {
                    case 'L':
                        num = possibleRotations.IndexOf(rotation) - 1;
                        if (num < 0)
                        {
                            num = 3;
                        }
                        rotation = possibleRotations[num];
                        break;
                    case 'R':
                        num = possibleRotations.IndexOf(rotation) + 1;
                        rotation = possibleRotations[num%4];
                        break;
                }
                move = int.Parse(commands[i].Substring(1));
                coords = movement(coords, move, rotation);
            }
            using (StreamWriter sw = new StreamWriter("cry.txt"))
            {
                map[coords.y][coords.x] = 'H';
                foreach (var item in mapCopy)
                {
                    foreach (var item1 in item)
                    {
                        sw.Write(item1);
                    }
                    sw.WriteLine();
                }
            }
            Console.WriteLine("Part 2: "+(coords.y*1000 + coords.x*4 + possibleRotations.IndexOf(rotation)));
        }

        static void Main(string[] args)
        {
            //part 1 is the same except the mapping is onto the opposite wall, much easier to visualise
            //make the map + 4 walls
            using (StreamReader sr = new StreamReader("inputMap.txt"))
            {
                map.Add((new string('~', 250)).ToCharArray().ToList());
                while (!sr.EndOfStream)
                {
                    List<char> line = sr.ReadLine().ToCharArray().ToList();
                    line.Insert(0, '~');
                    for (int i = 0; i < line.Count(); i++)
                    {
                        if (line[i] == ' ')
                        {
                            line[i] = '~';
                        }
                    }
                    for (int i = 0; i < 100; i++)
                    {
                        line.Add('~');
                    }
                    map.Add(line);
                }
                map.Add((new string('~', 250)).ToCharArray().ToList());
            }
            //parse the commands
            string command = File.ReadAllText("inputMoves.txt");
            int lastSplit = 0;
            for (int i = 0; i < command.Length; i++)
            {
                if (command[i] == 'L' || command[i] == 'R')
                {
                    commands.Add(command.Substring(lastSplit, i - lastSplit));
                    lastSplit = i;
                }
            }
            commands.Add(command.Substring(lastSplit, command.Length - lastSplit));

            foreach (var item in map)
            {
                List<char> temp = new List<char>();
                foreach (var item1 in item)
                {
                    temp.Add(item1);
                }
                mapCopy.Add(temp);
            }
            /* My cube shape:
                .##
                .#.
                ##.
                #..
            */
            //cube mapping edges to edges
            for (int i = 1; i < 51; i++)//1u-6d: 1u = (101,1) -> (150,1), 6d = (1,200) -> (50,200)
            {
                a2b.Add((100+i,1, 'u'), (i,200, 'd'));
            }
            for (int i = 1; i < 51; i++)//r1-r4: r1 = (150,1) -> (150,50), r4 = (100,150) -> (100,101)
            {
                a2b.Add((150, i, 'r'), (100, 151-i, 'r'));
            }
            for (int i = 1; i < 51; i++)//1d-r3: 1d = (101,50) -> (150,50), r3 = (100,51) -> (100,100)
            {
                a2b.Add((100+i, 50, 'd'), (100, 50+i, 'r'));
            }
            for (int i = 1; i < 51; i++)//2u-6l: 2u = (51,1) -> (100,1), 6l = (1,151) -> (1,200)
            {
                a2b.Add((50+i, 1, 'u'), (1, 150 + i, 'l'));
            }
            for (int i = 1; i < 51; i++)//r6-4d: r6 = (50,151) -> (50,200), 4d = (51,150) -> (100,150)
            {
                a2b.Add((50, 150+i, 'r'), (50+i, 150, 'd'));
            }
            for (int i = 1; i < 51; i++)//5u-3l: 5u = (1,101) -> (50,101), 3l = (51,51) -> (51,100)
            {
                a2b.Add((i, 101, 'u'), (51, 50+i, 'l'));
            }
            for (int i = 1; i < 51; i++)//5l-2l: 5l = (1,101) -> (1,150), 2l = (51,50) -> (51,1)
            {
                a2b.Add((1, 100+i, 'l'), (51, 51-i, 'l'));
            }

            //add the reverse for easy checking of keys
            var dictCopy = a2b.ToDictionary(entry => entry.Key, entry => entry.Value);
            foreach (var item in dictCopy)
            {
                a2b.Add((item.Value), (item.Key));
            }            

            part1();
            Console.ReadKey();
        }
    }
}
